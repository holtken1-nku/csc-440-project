#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import time
from constants import BASE_URI, API_TOKEN
import json
import requests


def standingsUpdater():
    from fdbAPI.models import Standings
    headers = {"X-Auth-Token": API_TOKEN}

    r = requests.get(f'{BASE_URI}/competitions', headers=headers)
    jsonData = json.loads(r.text)

    for num in range(len(jsonData["competitions"])):
        r = requests.get(f'{BASE_URI}/competitions/{jsonData["competitions"][num]["code"]}/standings',
                         headers=headers)
        jsonData2 = json.loads(r.text)
        for num2 in range(len(jsonData2['standings'])):
            for num3 in range(len(jsonData2['standings'][num2]['table'])):
                standings_data = {
                    'competitionCode_id': jsonData2['competition']['code'],
                    'seasonStage': jsonData2['standings'][num2]['stage'],
                    'teamId': jsonData2['standings'][num2]['table'][num3]['team']['id'],
                    'teamName': jsonData2['standings'][num2]['table'][num3]['team']['name'],
                    'position': jsonData2['standings'][num2]['table'][num3]['position'],
                    'playedGames': jsonData2['standings'][num2]['table'][num3]['playedGames'],
                    'gamesWon': jsonData2['standings'][num2]['table'][num3]['won'],
                    'gamesDrawn': jsonData2['standings'][num2]['table'][num3]['draw'],
                    'gamesLost': jsonData2['standings'][num2]['table'][num3]['lost'],
                    'points': jsonData2['standings'][num2]['table'][num3]['points'],
                    'goalsFor': jsonData2['standings'][num2]['table'][num3]['goalsFor'],
                    'goalsAgainst': jsonData2['standings'][num2]['table'][num3]['goalsAgainst'],
                }
                Standings.objects.update_or_create(
                    competitionCode_id=standings_data['competitionCode_id'],
                    seasonStage=standings_data['seasonStage'],
                    teamId=standings_data['teamId'],
                    defaults=standings_data
                )

        time.sleep(6.5)


def matchesUpdater():
    from fdbAPI.models import Matches
    headers = {"X-Auth-Token": API_TOKEN}

    r = requests.get(f'{BASE_URI}/competitions', headers=headers)
    jsonData = json.loads(r.text)

    for num in range(len(jsonData["competitions"])):
        r = requests.get(f'{BASE_URI}/competitions/{jsonData["competitions"][num]["code"]}/matches',
                         headers=headers)
        jsonData2 = json.loads(r.text)
        for num2 in range(len(jsonData2['matches'])):
            match_data = {
                'matchId': jsonData2['matches'][num2]['id'],
                'competitionCode_id': jsonData2['competition']['code'],
                'matchDateUTC': jsonData2['matches'][num2]['utcDate'],
                'updateDate': jsonData2['matches'][num2]['lastUpdated'],
                'homeTeamId': jsonData2['matches'][num2]['homeTeam']['id'],
                'homeTeamName': jsonData2['matches'][num2]['homeTeam']['name'],
                'awayTeamId': jsonData2['matches'][num2]['awayTeam']['id'],
                'awayTeamName': jsonData2['matches'][num2]['awayTeam']['name'],
                'winner': jsonData2['matches'][num2]['score']['winner'],
                'halfTimeHomeGoals': jsonData2['matches'][num2]['score']['halfTime']['home'],
                'halfTimeAwayGoals': jsonData2['matches'][num2]['score']['halfTime']['away'],
                'fullTimeHomeGoals': jsonData2['matches'][num2]['score']['fullTime']['home'],
                'fullTimeAwayGoals': jsonData2['matches'][num2]['score']['fullTime']['away'],
            }

            Matches.objects.update_or_create(
                matchId=match_data['matchId'],
                defaults=match_data
            )
        time.sleep(6.5)


def teamsUpdater():
    from fdbAPI.models import Teams

    headers = {"X-Auth-Token": API_TOKEN}

    r = requests.get(f'{BASE_URI}/competitions', headers=headers)
    jsonData = json.loads(r.text)

    for num in range(len(jsonData["competitions"])):
        r = requests.get(f'{BASE_URI}/competitions/{jsonData["competitions"][num]["code"]}/teams', headers=headers)
        jsonData2 = json.loads(r.text)
        for num2 in range(len(jsonData2['teams'])):
            team_data = {
                'teamId': jsonData2['teams'][num2]['id'],
                'competitionCode_id': jsonData2['competition']['code'],
                'name': jsonData2['teams'][num2]['name'],
                'founded': jsonData2['teams'][num2]['founded'],
                'venue': jsonData2['teams'][num2]['venue'],
                'coachName': jsonData2['teams'][num2]['coach']['name'],
                'squad': jsonData2['teams'][num2]['squad']
            }
            Teams.objects.update_or_create(
                teamId=team_data['teamId'],
                competitionCode_id=team_data['competitionCode_id'],
                defaults=team_data
            )
        time.sleep(6.5)


def competitionsUpdater():
    from fdbAPI.models import Competitions

    headers = {"X-Auth-Token": API_TOKEN}
    r = requests.get(f'{BASE_URI}/competitions', headers=headers)
    jsonData = json.loads(r.text)["competitions"]
    for num in range(len(jsonData)):
        competition_data = {
            'id': jsonData[num]['id'],
            'areaOfCompetition': jsonData[num]['area']['name'],
            'name': jsonData[num]['name'],
            'code': jsonData[num]['code'],
        }

        Competitions.objects.update_or_create(
            id=competition_data['id'],
            defaults=competition_data
        )


def updater():
    update = False
    if update:
        print("Updating Data")
        competitionsUpdater()
        teamsUpdater()
        matchesUpdater()
        standingsUpdater()
        print("Finished Updating")


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'csc440Final.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    updater()


if __name__ == '__main__':
    main()
