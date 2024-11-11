from pymongo import MongoClient


def load_competition(comp_dict, comp_code, sub_code):
    client = MongoClient()
    db = client["lucky_scarf"]

    if sub_code == "MTL":
        for match_dict in comp_dict["matches"]:
            db[f"{comp_code}_matchlist"].insert_one(match_dict)
    elif sub_code == "STN":
        for standings_dict in comp_dict["standings"][0]["table"]:
            db[f"{comp_code}_standings"].insert_one(standings_dict)
    elif sub_code == "TML":
        for team_dict in comp_dict["teams"]:
            db[f"{comp_code}_teamlist"].insert_one(team_dict)
