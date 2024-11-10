from env.constants import API_TOKEN
from src.extract import get_competition_data
# from src.load import load_competition
import json


def main():
    # Supported league competition codes:
    #   BL1 - German Bundesliga
    #   BSA - Brazilian Serie A
    #   DED - Dutch Eredivisie
    #   ELC - English League Championship
    #   FL1 - French Ligue 1
    #   PD  - Spanish Primera Division (La Liga)
    #   PL  - English Premier League
    #   PPL - Portuguese Primeira Liga
    #   SA  - Italian Serie A

    competition_code = "PL"
    competition_dict = get_competition_data(API_TOKEN, competition_code)

    print(json.dumps(competition_dict, indent=2))


if __name__ == "__main__":
    main()
