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
def fill_it_up():
    filler = Filler()
    start = time.time()
    x = 0
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
            filler.add_match(realdata)
            print(time.time() - start)
            x += 1

fill_it_up()
# json_obj = get_single_json()

# for x in json_objs:
#     filler.add_match(x)
#     print(time.time() - start)
