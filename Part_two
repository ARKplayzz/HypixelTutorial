import requests
from mojang import MojangAPI

api_key = "INSERT-YOUR-UUID"

userinput = str(input("Enter your minecraft username >>> "))

uuid = MojangAPI.get_uuid(userinput)
requestlink = f"https://api.hypixel.net/player?key={api_key}&uuid={uuid}"

hydata = requests.get(requestlink).json()

player = hydata["player"]["displayname"]

karma = hydata["player"]["karma"]
karma = "{:,}".format(karma)

print(f"{player} has {karma} karma")

logouttime = hydata['player']['lastLogout']
logintime = hydata['player']['lastLogin']

if logouttime < logintime:
    print(f'{player} is currently online')
else:
    print(f'{player} is currently offline')

try:
    rank = hydata['player']['newPackageRank']

    try:
        rank = hydata['player']['monthlyPackageRank']

        if rank == 'NONE':
            rank = hydata['player']['newPackageRank']
            
    except KeyError:
        pass

    if rank == 'VIP_PLUS':
        rank = 'VIP+'
    elif rank == 'MVP_PLUS':
        rank = 'MVP+'
    elif rank == 'SUPERSTAR':
        rank = 'MVP++'
    elif rank == 'NONE':
        raise KeyError

    print(f'{player} has the rank {rank}')

except KeyError:
    print(f'{player} does not have a rank')
