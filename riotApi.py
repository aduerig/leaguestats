import json
import requests
import time
import codecs
import os.path
import logging
import sys

logger = logging.getLogger('leaguestats.riotApi')


class RiotApi:
    def __init__(self, api_key, region='na'):
        self.myKey = api_key
        self.region = region
        self.dataC = {}
        self.dataT = {}


    def stopwatch(self, seconds):
        print('Waiting 1.3 seconds to prevent request overflow...')
        time.sleep(seconds)
        return

    def getlink(self, url, name):
        self.stopwatch(1.3)
        print(name.encode('utf-8'))
        data = json.loads(requests.get(url + self.myKey).text)
        return data

    def formaturl(self, url):
        url = url.format(self.region)
        return url

    def getchallenger(self):
        urlchallenger = 'https://{0}.api.pvp.net/api/lol/{0}/v2.5/league/challenger' \
                        '?type=RANKED_TEAM_5x5&api_key='
        self.dataC = self.getlink(self.formaturl(urlchallenger), 'Challenger Teams')
        logger.info('Successfully received data for all challenger teams')
        return self.dataC

    def getteam(self, name):
        for x in self.dataC['entries']:
            if name == x['playerOrTeamName']:
                teamid = str(x['playerOrTeamId'])
                teamname = str(x['playerOrTeamName']).replace('\ufb01', '')
                urlteam = 'https://{0}.api.pvp.net/api/lol/{0}/v2.4/team/' + teamid \
                                + '?api_key='
                self.dataT = self.getlink(self.formaturl(urlteam), teamname
                                     + ' Match History')  # Match history of team
                break
        return self.dataT[teamid]

    def getmatch(self, name, match):
        teamname = name.replace('\ufb01', '')
        for y in self.dataT:
            for x in self.dataT[y]['matchHistory']:
                if match == str(x['gameId']):
                    gameid = str(x['gameId'])
                    gamename = str('Match ' + gameid).replace('\ufb01', '')
                    urlmatch = 'https://{0}.api.pvp.net/api/lol/{0}/v2.2/match/' + gameid \
                               + '?includeTimeline=true' + '&api_key='
                    data = self.getlink(self.formaturl(urlmatch), gamename)  # Game of a team
                    break
        return data
