import json
import requests
import time
import os.path


class RiotApi:
    def __init__(self, api_key):
        self.myKey = api_key

    def stopwatch(self, seconds):
        start = time.time()
        time.clock()
        elapsed = 0
        print('Waiting 10 seconds to prevent request overflow...')
        while elapsed < seconds:
            elapsed = time.time() - start
            # print("loop cycle time: %f, seconds count: %02d" % (time.clock(), elapsed))
            time.sleep(1)
        return

    def getlink(self, url, name, path):
        if path != '':
            if not os.path.exists(path):
                os.makedirs(path)
        if not os.path.isfile(path + name + '.json'):
            self.stopwatch(10)
            print('Getting ' + name + '.json ' + 'from riot')
            data = json.loads(requests.get(url + self.myKey).text)
            with open(path + name + '.json', 'w') as f:
                json.dump(data, f)
            print('Saved!')
        else:
            print('Opening ' + name + '.json')
            with open(path + name + '.json') as f:
                data = json.load(f)
        return data

    def getchallenger(self):
        urlchallenger = 'https://na.api.pvp.net/api/lol/na/v2.5/league/challenger' \
                        '?type=RANKED_TEAM_5x5&api_key='
        data = self.getlink(urlchallenger, 'Challenger Teams', '/Challenger Stats/')
        return data

    def getteam(self, name):
        for x in self.getchallenger()['entries']:
            if name == x['playerOrTeamName']:
                teamid = str(x['playerOrTeamId'])
                teamname = str(x['playerOrTeamName']).replace('\ufb01', '')
                urlteam = 'https://na.api.pvp.net/api/lol/na/v2.4/team/' + teamid \
                                + '?api_key='
                data = self.getlink(urlteam, teamname
                                     + ' Match History', '/Challenger Stats/'
                                     + teamname + '/')  # Match history of team
                break
        return data[teamid]

    def getmatch(self, name, match):
        teamname = name.replace('\ufb01', '')
        for x in self.getteam(name)['matchHistory']:
            if match == str(x['gameId']):
                gameid = str(x['gameId'])
                gamename = str('Match ' + gameid).replace('\ufb01', '')
                urlmatch = 'https://na.api.pvp.net/api/lol/na/v2.2/match/' + gameid \
                           + '?includeTimeline=true' + '&api_key='
                data = self.getlink(urlmatch, gamename, '/Challenger Stats/' +
                                    teamname + '/' + gameid + '/')  # Game of a team
                break
        return data
