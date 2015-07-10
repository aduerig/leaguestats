from stats import *
from riotApi import *
from filler import Filler


api = RiotApi('70f53e5d-eea1-46f0-9e8a-19889489902f')

# Grabs challenger 5v5 teams
dataC = api.getchallenger()

# Outer loop running through all challenger teams (dataM)
def get_single_json():
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
            return realdata

json_obj = get_single_json()

filler = Filler()
filler.add_match(json_obj)
