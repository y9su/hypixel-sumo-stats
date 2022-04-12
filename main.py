import requests
import json
from mojang import MojangAPI
import time
from os import system
import colorama
from colorama import init, Fore
colorama.init()


while True:
    
    def getinfo(call):
        r = requests.get(call)
        return r.json()


    api = "" # Enter your Hypixel API key here

    username = input("Minecraft Username: ")
    uuid = MojangAPI.get_uuid(username)

    url = f"https://api.hypixel.net/player?key={api}&uuid={uuid}"

    data = getinfo(url)


    losses = data["player"]["stats"]["Duels"].get("sumo_duel_losses")
    wins = data["player"]["stats"]["Duels"]["sumo_duel_wins"]
    roundsplayed = data["player"]["stats"]["Duels"]["sumo_duel_rounds_played"]
    wlr = wins if losses is None else round((wins/losses), 2)


    if losses is None:
        print(Fore.RED + f"-> {username} has 0 sumo losses" + "\n")
    else:
        print(Fore.GREEN + f"-> {username} has {losses} sumo losses" + "\n")    
    print(Fore.GREEN + f"-> {username} has {wins} sumo wins" + "\n")
    print(Fore.GREEN + f"-> {username} has played {roundsplayed} games of sumo" + "\n")
    print(Fore.GREEN + f"-> {username} has a {wlr} WLR" + "\n" + Fore.WHITE)
    time.sleep(10)
    system("cls")
