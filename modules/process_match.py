from modules.data_processing import rankings, player_profile, previous_encounters
import datetime

from keras.models import load_model
from keras.utils import CustomObjectScope
from keras.initializers import glorot_uniform
from keras.backend import clear_session
import pandas as pd


def preprocess(player1, player2, type, gender):
    """
    (str, str, str, str) -> list
    Process the data before using in neural network.
    :param player1: first player name
    :param player2: second player name
    :param type: type of court
    :param gender: gender of players
    :return: list
    """
    player1, player2 = ", ".join(player1.split()), ", ".join(player2.split())
    gender = 1 if gender == "male" else 0
    r = rankings(gender)
    type = type.capitalize()

    for rank in r:
        if rank[2] == player1:
            id1 = rank[1]
        elif rank[2] == player2:
            id2 = rank[1]

    rankings_path = "data/men_rankings.txt" if gender else "data/women_rankings.txt"
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
    """
    (float, float, float, int) -> int
    Predict the outcome of match by given values using neural network.
    :param ranking: ranking data
    :param surface: surface performance data
    :param previous: previous encounters data
    :param gender: 0 for female, 1 for male
    :return: predicted chance of first player winning
    """
    path = "neural_network/men_tennis.h5" if gender else "neural_network/women_tennis.h5"

    with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
        model = load_model(path)
    prediction = model.predict(pd.DataFrame.from_dict({"ranking": [ranking], "surface": [surface], "previous": [previous]}))

    clear_session()

    return int((1 - prediction[0][0]) * 100)


def process_match(player1, player2, type, gender):
    """
    (str, str, str, str) -> int
    Process the data and predict the outcome of a match.
    :param player1: first player name
    :param player2: second player name
    :param type: type of court
    :param gender: gender of players
    :return:
    """
    data = preprocess(player1, player2, type, gender)
    ranking, surface, previous, gender = data[4], data[5], data[6], data[7]

    return predict_match(ranking, surface, previous, gender)
