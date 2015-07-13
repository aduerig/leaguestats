import json
import requests
import time
import codecs
import os.path


class RiotApi:
    def __init__(self, api_key):
        self.myKey = api_key
        self.dataC = {}
        self.dataT = {}

    def stopwatch(self, seconds):
        print('Waiting 10 seconds to prevent request overflow...')
        time.sleep(seconds)
        return

    def getlink(self, url, name, path):
        self.stopwatch(1.3)
        name = name.encode('utf-8')
        print('Getting ' + name + '.json ' + 'from riot')
        data = json.loads(requests.get(url + self.myKey).text)
        return data

    def getchallenger(self):
        urlchallenger = 'https://na.api.pvp.net/api/lol/na/v2.5/league/challenger' \
                        '?type=RANKED_TEAM_5x5&api_key='
        self.dataC = self.getlink(urlchallenger, 'Challenger Teams', '/Challenger Stats/')
        return self.dataC

    def getteam(self, name):
        for x in self.dataC['entries']:
            if name == x['playerOrTeamName']:
                teamid = str(x['playerOrTeamId'])
                teamname = str(x['playerOrTeamName']).replace('\ufb01', '')
                urlteam = 'https://na.api.pvp.net/api/lol/na/v2.4/team/' + teamid \
                                + '?api_key='
                self.dataT = self.getlink(urlteam, teamname
                                     + ' Match History', '/Challenger Stats/'
                                     + teamname + '/')  # Match history of team
                break
        return self.dataT[teamid]

    def getmatch(self, name, match):
        teamname = name.replace('\ufb01', '')
        for y in self.dataT:
            for x in self.dataT[y]['matchHistory']:
                if match == str(x['gameId']):
                    gameid = str(x['gameId'])
                    gamename = str('Match ' + gameid).replace('\ufb01', '')
                    urlmatch = 'https://na.api.pvp.net/api/lol/na/v2.2/match/' + gameid \
                               + '?includeTimeline=true' + '&api_key='
                    data = self.getlink(urlmatch, gamename, '/Challenger Stats/' +
                                        teamname + '/' + gameid + '/')  # Game of a team
                    break
        return data
