from stats import *
from riotApi import *
from filler import Filler
from database import *
import time
import logging
import logging.handlers


logger = logging.getLogger('leaguestats')
logger.setLevel(logging.INFO)
timed_log = logging.handlers.TimedRotatingFileHandler('fill.log', when='W0', interval=4)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
timed_log.setFormatter(formatter)
logger.addHandler(timed_log)

regions = ['lan', 'kr', 'br', 'eune', 'euw', 'na', 'oce', 'ru', 'tr']

# Outer loop running through all challenger teams (dataM)
def fill_it_up():
    filler = Filler()
    start = time.time()
    for region in regions:
        api = RiotApi('70f53e5d-eea1-46f0-9e8a-19889489902f', region)
        dataC = api.getchallenger()
        x = 0
        for g in dataC['entries']:
            y = 0
            dataT = api.getteam(g['playerOrTeamName'])
            # Grabs all games form a team (dataT)
            for j in dataT['matchHistory']:
                match = filler.session.query(MatchDetail).\
                    filter(MatchDetail.matchId == j['gameId']).first()
                if match is not None:
                    continue
                try:
                    dataM = api.getmatch(g['playerOrTeamName'], str(j['gameId']))
                except:
                    logger.exception('Exception while calling getmatch on team \"%s\" match %s',
                                     g['playerOrTeamName'].encode('utf-8'), str(j['gameId']).encode('utf-8'))
                    continue
                try:
                    statgetter = GetStats(dataM)
                    realdata = statgetter.returnMatchDetail()
                except:
                    logger.exception('Exception while creating statgetter on team \"%s\" match %s',
                                     g['playerOrTeamName'].encode('utf-8'), str(j['gameId']).encode('utf-8'))
                    continue
                filler.add_match(realdata)
                print(time.time() - start)
                logger.info('Successfully added team \"%s\" match %s', g['playerOrTeamName'].encode('utf-8'),
                            str(j['gameId']).encode('utf-8'))
                x += 1
            logger.info('Finished adding all matches for team \"%s\"', g['playerOrTeamName'].encode('utf-8'))
        logger.info('Finished adding all matches for region %s', region)

fill_it_up()
