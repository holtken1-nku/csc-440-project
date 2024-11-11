from env.constants import BASE_URI
import json
import requests


def get_competition(auth_key, comp_code, sub_code):
    uri = f"{BASE_URI}/competitions/{comp_code}"

    if sub_code == "MTL":
        uri += "/matches"
    elif sub_code == "STN":
        uri += "/standings"
    elif sub_code == "TML":
        uri += "/teams"

    headers = {"X-Auth-Token": auth_key}

    try:
        r = requests.get(uri, headers=headers)
        return json.loads(r.text)
    except requests.exceptions.RequestException:
        print("An exception occurred.")
