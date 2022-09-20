# Learning Python right now... =^._.^= ∫ meow

from datetime import datetime
import requests

key = "87f9c6a6-aff6-4fcf-9416-051dff4b6bc7"

def checkUserAccount():
    number = input("Type 1 for Hypixel Stats check; Type 2 for Minecraft-Account Information: ")
    if number == "1":
        username = input()

        # Mojang API
        playerUUID = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}").json()
        playerId = playerUUID['id']

        # Hypixel API
        playerInformation = requests.get(f"https://api.hypixel.net/player?key={key}&uuid={playerId}").json()
        

        # Terminal Anzeigen
        try:
            print("\nHypixel-Stats information: \n")
            print("Rank: " + playerInformation["player"]["newPackageRank"])
            print("Username: " + playerInformation["player"]["displayname"])
           
        except KeyError:
            print("")
            print("Rank: player")
            print("Username: " + playerInformation["player"]["displayname"])
        return
    
    if number == "2":
        username = input("Enter Minecraft-Username: ")

        # Mojang API
        api = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}").json()
        playerId = api['id']

        # Gapple API

        statusCheck = requests.get(f"https://api.gapple.pw/status/{playerId}").json()
        status = statusCheck["status"]
        if status == "msa" or status == "microsoft":
            status = "Microsoft"
            print("\nUsername: " + api["name"])
            print("Status: " + status)

checkUserAccount()
