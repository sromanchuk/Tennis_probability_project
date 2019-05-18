import http.client
import json
import time
import datetime


def get_json(source):
    conn = http.client.HTTPSConnection("api.sportradar.us")
    conn.request("GET", source)
    res = conn.getresponse()
    json_data = res.read().decode("utf-8")
    json_data = json.loads(json_data)
    time.sleep(1)
    return json_data


def rankings(gender):
    """
    (str) -> lst
    :param gender: 0 for female rankings, 1 for male rankings
    :return: list containing rankings
    """
    json_data = get_json("/tennis-t2/en/players/rankings.json?api_key=8vfgwpuch3rpnauqm9cbzp7d")

    ranking = json_data["rankings"][gender]["player_rankings"]
    ranking_list = []

    for rank in ranking:
        ranking_list.append((rank["rank"], rank["player"]["id"], rank["player"]["name"]))

    return ranking_list


def player_profile(id, rankings_path):
    json_data = get_json("/tennis-t2/en/players/{}/profile.json?api_key=8vfgwpuch3rpnauqm9cbzp7d".format(id))
    rankings_data = []
    with open(rankings_path) as f:
        for line in f:
            rankings_data.append(line.strip().split())
    profile = [json_data["player"]["id"], json_data["player"]["name"], rank(id, rankings_data),
               surface_stats(json_data)]
    return profile


def surface_stats(data):
    stats = data["statistics"]["periods"]
    surfaces = {"Red clay": [0, 0], "Grass": [0, 0], "Hardcourt outdoor": [0, 0], "Hardcourt indoor": [0, 0]}

    for i in range(5):
        try:
            for surface in stats[i]["surfaces"]:
                if surface["type"] in ["Red clay", "Grass", "Hardcourt outdoor", "Hardcourt indoor"]:
                    surfaces[surface["type"]][0] += surface["statistics"]["matches_played"]
                    surfaces[surface["type"]][1] += surface["statistics"]["matches_won"]
        except IndexError:
            print(IndexError)

    for surface in surfaces:
        if surfaces[surface] == [0, 0]:
            surfaces[surface] = 0.5
        else:
            surfaces[surface] = round(surfaces[surface][1] / surfaces[surface][0], 3)

    return surfaces


def rank(id, rankings):
    r = 0
    for rank in rankings:
        if id == rank[1]:
            r = int(rank[0])
    return r


def matches_from_tournaments(file):
    print(file)
    f = open(file).read()
    tournaments_list = json.loads(f)["tournaments"]
    matches = []
    try:
        for i in range(20):
            json_data = get_json("/tennis-t2/en/tournaments/{}/schedule.json?api_key=rzx3rjfpscjz2n724zf46n32".format(tournaments_list[i]["id"]))
            tour_matches = [i["id"] for i in json_data["sport_events"]]
            for match in tour_matches:
                matches.append(match)
            print(matches)
            time.sleep(1)
    except json.decoder.JSONDecodeError:
        pass
    return matches


def previous_encounters(id1, id2, date):
    try:
        matches = get_json("/tennis-t2/en/players/{}/versus/{}/matches.json?api_key=8vfgwpuch3rpnauqm9cbzp7d".format(id1, id2))["last_meetings"]["results"]
    except TypeError:
        return 0.5
    wins1, wins2 = 0, 0
    for match in matches:
        match_date = datetime.datetime.strptime(match["sport_event"]["scheduled"][:10], "%Y-%m-%d")
        if match_date < date:
            winner = match["sport_event_status"]["winner_id"]
            if winner == id1:
                wins1 += 1
            elif winner == id2:
                wins2 += 1
        else:
            continue
    if wins1 or wins2:
        winrate = round(wins2 / (wins1 + wins2), 3)
    else:
        return 0.5
    return winrate


def tournaments(file, gender):
    f = open("tournaments.txt").read()
    tournaments_list = json.loads(f)["tournaments"]
    result = [i for i in tournaments_list if i["gender"] == gender and i["type"] == "singles"]
    result = {"tournaments": result}
    return result


# if __name__ == "__main__":
#     json_data = get_json("/web_app-t2/en/players/sr:competitor:129368/profile.json?api_key=8vfgwpuch3rpnauqm9cbzp7d")
#     json_data = json.dumps(json_data, indent=2)
#     print(json_data)