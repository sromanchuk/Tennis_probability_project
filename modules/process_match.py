from modules.data_processing import rankings, player_profile, previous_encounters
import datetime

from keras.models import load_model
from keras.utils import CustomObjectScope
from keras.initializers import glorot_uniform
import pandas as pd


def preprocess(player1, player2, type, gender):
    print(player1, player2)
    print(gender)
    player1, player2 = ", ".join(player1.split()), ", ".join(player2.split())
    gender = 1 if gender == "male" else 0
    print(gender)
    r = rankings(gender)
    type = type.capitalize()
    print(r)
    print(gender)
    print(player1, player2)
    for rank in r:
        if rank[2] == player1:
            id1 = rank[1]
        elif rank[2] == player2:
            id2 = rank[1]
    rankings_path = "../data/men_rankings.txt" if gender else "women_rankings.txt"
    profile1, profile2 = player_profile(id1, rankings_path), player_profile(id2, rankings_path)
    rank1, rank2 = profile1[2], profile2[2]
    if rank1 == 0 or rank2 == 0:
        return None
    rank_data = round((rank1 / len(r) + (1 - rank2 / len(r))) / 2, 3)
    surface_stats1, surface_stats2 = profile1[3][type], profile2[3][type]
    surface_data = round(((1 - surface_stats1) + surface_stats2) / 2, 3)
    date = datetime.datetime.now()
    previous_data = previous_encounters(profile1[0], profile2[0], date)
    return [profile1[0], profile1[1].replace(",", ""), profile2[0], profile2[1].replace(",", ""), str(rank_data),
            str(surface_data), str(previous_data), gender]


def predict_match(ranking, surface, previous, gender):
    path = "../neural_network/my_model.h5" if gender else ""
    with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
        model = load_model(path)
    prediction = model.predict(pd.DataFrame.from_dict({"ranking": [ranking], "surface": [surface], "previous": [previous]}))
    return int((1 - prediction[0][0]) * 100)


def process_match(player1, player2, type, gender):
    data = preprocess(player1, player2, type, gender)
    ranking, surface, previous, gender = data[4], data[5], data[6], data[7]
    return predict_match(ranking, surface, previous, gender)
