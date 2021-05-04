import requests
from mojang import MojangAPI

userinput = str(input("Enter your minecraft username >>> "))

uuid = MojangAPI.get_uuid(userinput)
requestlink = str("https://api.hypixel.net/player?key=73a31f3e-7d06-477d-8f53-1157e6a183bd&uuid="+ uuid)

hydata = requests.get(requestlink).json()

player = hydata["player"]["displayname"]

karma = hydata["player"]["karma"]
karma = "{:,}".format(karma)

print(f"{player} has {karma} karma")
