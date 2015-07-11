from stats import *
from riotApi import *
from filler import Filler
import time


api = RiotApi('70f53e5d-eea1-46f0-9e8a-19889489902f')

# Grabs challenger 5v5 teams
dataC = api.getchallenger()
with open('challenger_data.txt', 'w') as outfile:
        json.dump(dataC, outfile, indent=2, separators=(',', ': '))

# Outer loop running through all challenger teams (dataM)
def get_single_json():
    x = 0
    arr = []
    for g in dataC['entries']:
        y = 0
        dataT = api.getteam(g['playerOrTeamName'])
        # Grabs all games form a team (dataT)
        for j in dataT['matchHistory']:
            dataM = api.getmatch(g['playerOrTeamName'], str(j['gameId']))
            statgetter = GetStats(dataM)
            realdata = statgetter.returnMatchDetail()
            # with open('/Challenger Stats/test.txt', 'w') as outfile:
            #     json.dump(realdata,  outfile, indent=4, separators=(',', ': '))
            arr.append(realdata)
            x += 1
        if x >= 20:
            break
    return arr

json_objs = get_single_json()
# json_obj = get_single_json()

filler = Filler()
start = time.time()
for x in json_objs:
    filler.add_match(x)
    print(time.time() - start)
