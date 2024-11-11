from env.constants import API_TOKEN
from src.extract import get_competition
from src.load import load_competition


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

    # Supported subresource codes:
    #   MTL  - Match list
    #   STN  - Standings
    #   TML  - Team list

    subresource_code = "MTL"

    competition_dict = get_competition(API_TOKEN, competition_code, subresource_code)
    load_competition(competition_dict, competition_code, subresource_code)


if __name__ == "__main__":
    main()
