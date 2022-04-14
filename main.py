import requests
import json
from mojang import MojangAPI
import time
import sys


while True:
    
    def getinfo(call):
        r = requests.get(call)
        return r.json()


    api = json.loads(open("config.json").read())['api']

    username = input("Minecraft Username: ")
    uuid = MojangAPI.get_uuid(username)

    url = f"https://api.hypixel.net/player?key={api}&uuid={uuid}"
    webhook = json.loads(open("config.json").read())['webhook']

    data = getinfo(url)


    losses = data["player"]["stats"]["Duels"].get("sumo_duel_losses")
    wins = data["player"]["stats"]["Duels"].get("sumo_duel_wins", 0)
    roundsplayed = data["player"]["stats"]["Duels"].get("sumo_duel_rounds_played", 0)
    wlr = wins if losses is None else round((wins/losses), 2)


    if losses is None:
        losses1 = f"**{username}** has __***0***__ sumo losses" + "\n"
    else:
        losses1 = f"**{username}** has __***{losses}***__ sumo losses" + "\n"
    wins1 = f"**{username}** has __***{wins}***__ sumo wins" + "\n"
    roundsplayed1 = f"**{username}** has played __***{roundsplayed}***__ games of sumo" + "\n"
    wlr1 = f"**{username}** has a __***{wlr}***__ WLR" + "\n"
    
    wlr_dangerous = json.loads(open("config.json").read())['wlr_dangerous']
    if wlr > wlr_dangerous:
        color = "15076352"
        danger = f"**{username}** is a **dangerous** opponent!"
    else:
        color = "58892"
        danger = f"**{username}** is **not** a dangerous opponent!"
        

    webhook_message = {
        "embeds": [{
            "title": "``Stats:`` ",
            "description": f"{losses1}{wins1}{roundsplayed1}{wlr1}\n{danger}",
            "color": color
            }]
    }
    
    
    response = requests.post(webhook, json=webhook_message)
    print("Stats sent to webhook!\nClosing file in 10 seconds")
    time.sleep(10)
    sys.exit()
