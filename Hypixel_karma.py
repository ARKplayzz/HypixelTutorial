  
import requests
from mojang import MojangAPI

userinput = str(input("Enter your minecraft username >>> "))

uuid = MojangAPI.get_uuid(userinput)
requestlink = str("https://api.hypixel.net/player?key= API KEY &uuid="+ uuid)

hydata = requests.get(requestlink).json()

player = hydata["player"]["displayname"]

karma = hydata["player"]["karma"]
karma = "{:,}".format(karma)

print(f"{player} has {karma} karma")
