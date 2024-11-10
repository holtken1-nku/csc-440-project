from env.constants import BASE_URI
import json
import requests


def get_competition_data(auth_key, comp_code, subresource=""):
    uri = f"{BASE_URI}/competitions/{comp_code}"

    if subresource == "matches":
        uri += "/matches"
    elif subresource == "standings":
        uri += "/standings"
    elif subresource == "teams":
        uri += "/teams"

    headers = {"X-Auth-Token": auth_key}

    try:
        r = requests.get(uri, headers=headers)
        return json.loads(r.text)
    except requests.exceptions.RequestException:
        print("An exception occurred.")
