import requests
from config import DISCLOUD_API, HEADERS

def check_discord_api():
    try:
        r = requests.get("https://discordstatus.com/api/v2/status.json")
        return r.json()['status']['indicator'] == 'none'
    except:
        return False

def check_bot_discloud():
    try:
        r = requests.get(DISCLOUD_API, headers=HEADERS)
        return r.json()["app"]["online"]
    except:
        return False