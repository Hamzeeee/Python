# Learning Python right now... =^._.^= ∫ meow

from datetime import datetime
import requests

hypixel_api_key = "<INSERT KEY HERE>"

def checkUserAccount():
    number = input("Type 1 for Hypixel Stats check; Type 2 for Minecraft-Account Information:\n")
    
    if number == "1":
        username = input()

        # Mojang API
        mojang_player = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}").json()
        player_uuid = mojang_player['id']

        # Hypixel API
        hypixel_player_information = requests.get(f"https://api.hypixel.net/player?key={hypixel_api_key}&uuid={player_uuid}").json()
        

        # Print in Terminal
        try:
            print("\nHypixel-Stats information: \n")
            print("Rank: " + hypixel_player_information["player"]["newPackageRank"])
            print("Username: " + hypixel_player_information["player"]["displayname"])
           
        except KeyError:
            print("")
            print("Rank: player")
            print("Username: " + hypixel_player_information["player"]["displayname"])
        return
    
    if number == "2":
        username = input("Enter Minecraft-Username: ")

        # Mojang API
        mojang_player = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}").json()
        player_uuid = mojang_player['id']

        # Gapple API

        statusCheck = requests.get(f"https://api.gapple.pw/status/{player_uuid}").json()
        status = statusCheck["status"]
        if status == "msa" or status == "microsoft":
            status = "Microsoft"
            print("\nUsername: " + mojang_player["name"])
            print("Status: " + status)


if __name__ == '__main__':
    checkUserAccount()
