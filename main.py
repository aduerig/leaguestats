#Key start
# 70f53e5d-eea1-46f0-9e8a-19889489902f
#Key end

import requests
import os.path
import time
import json
from stats import *
from riotApi import *
from filler import Filler
from database import *


myKey = '70f53e5d-eea1-46f0-9e8a-19889489902f'


#nsample = 100
#x = numpy.linspace(0, 10, 100)
#X = numpy.column_stack((x, x**2))
#beta = numpy.array([1, 0.1, 10])
#e = numpy.random.normal(size=nsample)
#print(e)

def stopwatch(seconds):
    start = time.time()
    time.clock()
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        print("loop cycle time: %f, seconds count: %02d" % (time.clock(), elapsed) )
        time.sleep(1)

#if not os.path.exists('/Challenger Stats/'):
    #os.makedirs('/Challenger Stats/')

def getLink( url, name, path ):
    print(url)
    print(name)
    print(path)
    if path != '':
        if not os.path.exists(path):
            os.makedirs(path)
    if os.path.isfile(path + name + '.json') == False:
        #calls += 1
        #if calls >= callsPerTen:
            #stopwatch(10)zs
        print('Getting ' + name + '.json ' + 'from riot')
        stopwatch(10)
        data = json.loads(requests.get(url + myKey).text)
        with open(path + name + '.json', 'w') as f:
            json.dump(data, f)
        print('Saved!')
    else:
        print('Opening ' + name + '.json')
        with open(path + name + '.json') as f:
            data = json.load(f)
    return data


print('\n')


# dataM = getLink('ayy', 'Challenger Teams', '/Challenger Stats/')
# teamName = dataM['entries'][0]['playerOrTeamName']
# dataT = getLink('lmao', teamName + ' Match History', '/Challenger Stats/' + teamName + '/')
# teamId = dataM['entries'][0]['playerOrTeamId']
# gameName = teamName + ' Match ' + str(dataT[teamId]['matchHistory'][0]['gameId'])
# dataG = getLink('dank', gameName, '/Challenger Stats/' + teamName + '/' + str(dataT[teamId]['matchHistory'][0]['gameId']) + '/')
# gameId = str(dataT[teamId]['matchHistory'][0]['gameId'])



# print(statGetter.returnMatchDetail(dataG))
# print(statGetter.returnParticipant(dataG['participants'][0]))
# print(statGetter.returnParticipantIdentity(dataG['participantIdentities'][0]))
# print(statGetter.returnTeam(dataG['teams'][0]))
# print(statGetter.returnTimeline(dataG['timeline']))
# print(statGetter.returnMastery(dataG['participants'][0]['masteries'][0]))
# print(statGetter.returnParticipantStats(dataG['participants'][0]['stats']))
# print(statGetter.returnParticipantTimeline(dataG['participants'][0]['timeline']))
# print(statGetter.returnRune(dataG['participants'][0]['runes'][0]))
# print(statGetter.returnPlayer(dataG['participantIdentities'][0]['player']))
# print(statGetter.returnBannedChampion(dataG['teams'][0]['bans'][0]))
# print(statGetter.returnFrame(dataG['timeline']['frames'][0]))
# print(statGetter.returnParticipantTimelineData(dataG['participants'][0]['timeline']['csDiffPerMinDeltas']))
# print(statGetter.returnEvent(dataG['timeline']['frames'][1]['events'][0]))
# print(statGetter.returnParticipantFrame(dataG['timeline']['frames'][1]['participantFrames']['1']))
# print(statGetter.returnPosition(dataG['timeline']['frames'][1]['participantFrames']['1']))



"""
if(dataG["teams"][0]['teamId'] == 100):
    blueTeam = dataG["teams"][0]
    purpleTeam = dataG["teams"][1]
else:
    blueTeam = dataG["teams"][1]
    purpleTeam = dataG["teams"][0]


dragonKillsBlue = blueTeam['dragonKills']
print(dragonKillsBlue)
print(dataG.keys())
print(len(dataG['timeline']['frames']))
print(dataG['timeline']['frames'][1])

with open('/Challenger Stats/' + teamName + '/' + gameId + '/' + gameName + ' random ass stats' + '.txt', 'w') as outfile:
    json.dump(dataG['timeline']['frames'][1],  outfile, indent=4, separators=(',', ': '))



print('\n')

with open('/Challenger Stats/' + teamName + '/' + gameId + '/' + gameName + '.txt', 'w') as outfile:
    json.dump(dataG,  outfile, indent=4, separators=(',', ': '))
"""

#dataTest = getLink('blah', 'Challenger Teams', '/Challenger Stats/')

#f = csv.writer(open("test.csv", "wb+"))

# Write CSV Header, If you dont need that, remove this line
#f.writerow(["pk", "model", "codename", "name", "content_type"])

#for x in x:
#    f.writerow([x["pk"],
#                x["model"],
#                x["fields"]["codename"],
#                x["fields"]["name"],
#                x["fields"]["content_type"]])




#Grabs challenger 5v5 teams
urlChallenger = 'https://na.api.pvp.net/api/lol/na/v2.5/league/challenger?type=RANKED_TEAM_5x5&api_key='
dataM = getLink(urlChallenger, 'Challenger Teams', '/Challenger Stats/')
with open('/Challenger Stats/' + 'Challenger Teams' + '.txt', 'w') as outfile:
        json.dump(dataM,  outfile, indent=4, separators=(',', ': '))

#Outer loop running through all challenger teams (dataM)
for g in range(len(dataM['entries'])):
    teamId = dataM['entries'][g]['playerOrTeamId']
    teamName = str(dataM['entries'][g]['playerOrTeamName']).replace('\ufb01', '')
    urlChallengerTeam = 'https://na.api.pvp.net/api/lol/na/v2.4/team/' + teamId + '?api_key='
    dataT = getLink(urlChallengerTeam, teamName + ' Match History', '/Challenger Stats/' + teamName + '/') #Match history of team
    with open('/Challenger Stats/' + teamName + '/' + teamName + ' Match History' + '.txt', 'w') as outfile:
            json.dump(dataT,  outfile, indent=4, separators=(',', ': '))

    #Grabs all games form a team (dataT)


    for j in range(len(dataT[teamId]['matchHistory'])):
        gameId = str(dataT[teamId]['matchHistory'][j]['gameId'])
        gameName = str(teamName + ' Match ' + gameId).replace('\ufb01', '')
        urlChallengerTeamMatch = 'https://na.api.pvp.net/api/lol/na/v2.2/match/' + gameId + '?includeTimeline=true' + '&api_key='
        dataG = getLink(urlChallengerTeamMatch, gameName, '/Challenger Stats/' + teamName + '/' + gameId + '/') #Game of a team


        statGetter = GetStats(dataG)
        # matchObj = statGetter.returnMatchDetail()
        # pIdList = statGetter.returnParticipantIdentityList()
        # fillIt = Filler()
        # fillIt.session.add(MatchDetail(**matchObj))
        # sqlMatch = fillIt.session.query(MatchDetail).filter(MatchDetail.matchId == matchObj['matchId']).first()
        # arr = []
        # for x in pIdList:
        #     arr.append(ParticipantIdentity(**x))
        # sqlMatch.participantIdentities = arr
        # fillIt.session.commit()
        # fillIt.session.close()

        # print(statGetter.returnEventList())
        # print(statGetter.returnParticipantList())
        # print(statGetter.returnTeamList())
        # print(statGetter.returnMasteryList())
        # print(statGetter.returnParticipantStatsList())
        # print(statGetter.returnParticipantTimelineList())
        # print(statGetter.returnRuneList())
        print(statGetter.returnPlayerList())
        # print(statGetter.returnBannedChampionList())
        # print(statGetter.returnFrameList())
        # print(statGetter.returnParticipantTimelineDataList())
        # print(statGetter.returnParticipantFrameList())
        # print(statGetter.returnPositionList())
        # print(statGetter.returnFrameList())



        if(j == 0):
            break

        with open('/Challenger Stats/' + teamName + '/' + gameId + '/' + gameName + '.txt', 'w') as outfile:
                json.dump(dataG,  outfile, indent=4, separators=(',', ': '))

    if(g == 0):
        break




#print(dataM.keys())
#print(len(dataM['entries']))

#print(dataM['entries'][0].keys())
#print(dataM['entries'][0]['playerOrTeamName'])
#print(dataM['entries'][0]['playerOrTeamId'])

#print(dataT.keys())
#print(dataT[dataM['entries'][0]['playerOrTeamId']].keys())
#print(dataT[dataM['entries'][0]['playerOrTeamId']]['matchHistory'])
#print(dataT[dataM['entries'][0]['playerOrTeamId']]['matchHistory'][0]['gameId'])


#for j in range(2):
#    print(dataM)
#    print(dataT)
#    print(dataM['entries'][0]['playerOrTeamId'])
#    print(dataM['entries'][1]['playerOrTeamId'])
#    print(dataT.keys())
#    print(j)
#    urlChallengerTeamMatch = 'https://na.api.pvp.net/api/lol/na/v2.2/match/' + str(dataT[dataM['entries'][j]['playerOrTeamId']]['matchHistory'][j]['gameId']) + '?includeTimeline=true' + '&api_key='
#    gameName = dataM['entries'][j]['playerOrTeamName'] + ' Match ' + str(dataT[dataM['entries'][j]['playerOrTeamId']]['matchHistory'][j]['gameId'])
#    dataG = getLink(urlChallengerTeamMatch, gameName, '/Challenger Stats/' + dataM['entries'][j]['playerOrTeamName'] + '/' + str(dataT[dataM['entries'][j]['playerOrTeamId']]['matchHistory'][j]['gameId']) + '/') #Game of a team
#    with open('/Challenger Stats/' + dataM['entries'][j]['playerOrTeamName'] + '/' + str(dataT[dataM['entries'][j]['playerOrTeamId']]['matchHistory'][j]['gameId']) + '/' + gameName + '.txt', 'w') as outfile:
#            json.dump(dataG,  outfile, indent=4, separators=(',', ': '))







"""
x = 2 #Number of names

dataJ = [{} for i in range(x)]

urlPeople = ["a"] * x
ID = ["a"] * x
ID[0] = 'D U R nlaW'
ID[1] = 'ScrubFLoorHyrule'

for i in range(x):
    ID[i] = ID[i].replace(" ", "").lower().strip(' \t\n\r')
    urlPeople[i] = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/' + ID[i] + '?api_key='
    if(os.path.isfile(ID[i] + '.json') == False):
        print("open")
        dataJ[i] = json.loads(requests.get(urlPeople[i] + myKey).text)
        with open(ID[i] + '.json', 'w') as f:
            json.dump(dataJ[i], f)
    else:
        print("no open")
        with open(ID[i] + '.json') as f:
            dataJ[i] = json.load(f)

print(dataJ[0][ID[0]].keys())
print('id' in dataJ[0][ID[0]])


#with open(str(userID) + '.txt', 'w') as outfile:
        #json.dump(dataJ,  outfile, indent=4, separators=(',', ': '))

#print('summonerLevel' in dataJ)

#jdata = json.load('{"uri": "http:", "foo", "bar"}')
#print('uri' in jdata)

#summonerLevel = json[userID].summonerLevel
#summonerID = json[userID].id

#print(summonerLevel)

#document.getElementById("sLevel").innerHTML = summonerLevel;
#document.getElementById("sID").innerHTML = summonerID;

"""