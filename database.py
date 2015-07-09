from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class MatchDetail(Base):
    __tablename__ = 'match_detail'

    mapId = Column(Integer)
    matchCreation = Column(BigInteger)
    matchDuration = Column(BigInteger)
    matchId = Column(BigInteger, primary_key=True)
    matchMode = Column(String)
    matchType = Column(String)
    matchVersion = Column(String)
    platformId = Column(String)
    queueType = Column(String)
    region = Column(String)
    season = Column(String)

# Set relation
class Participant(Base):
    __tablename__ = 'participant'

    championId = Column(Integer)
    highestAchievedSeasonTier = Column(String)
    participantId = Column(Integer)
    spell1Id = Column(Integer)
    spell2Id = Column(Integer)
    teamId = Column(Integer)

# Add relations
class ParticipantIdentity(Base):
    __tablename__ = 'participant_identity'

    participantId = Column(Integer)


class Team(Base):
    __tablename__ = 'team'

    baronKills = Column(Integer)
    dominionVictoryScore = Column(BigInteger)
    dragonKills = Column(Integer)
    firstBaron = Column(Boolean)
    firstBlood = Column(Boolean)
    firstDragon = Column(Boolean)
    firstInhibitor = Column(Boolean)
    firstTower = Column(Boolean)
    inhibitorKills = Column(Integer)
    teamId = Column(Integer)
    towerKills = Column(Integer)
    vilemawKills = Column(Integer)
    winner = Column(Boolean)


class Timeline(Base):
    __tablename__ = 'timeline'

    frameInterval = Column(BigInteger)


class Mastery(Base):
    __tablename__ = 'mastery'

    masteryId = Column(BigInteger)
    rank = Column(BigInteger)


class ParticipantStats(Base):
    __tablename__ = 'participant_stats'

    assists = Column(BigInteger)
    champLevel = Column(BigInteger)
    combatPlayerScore = Column(BigInteger)
    deaths = Column(BigInteger)
    doubleKills = Column(BigInteger)
    firstBloodAssist = Column(Boolean)
    firstBloodKill = Column(Boolean)
    firstInhibitorAssist = Column(Boolean)
    firstInhibitorKill = Column(Boolean)
    firstTowerAssist = Column(Boolean)
    firstTowerKill = Column(Boolean)
    goldEarned = Column(BigInteger)
    goldSpent = Column(BigInteger)
    inhibitorKills = Column(BigInteger)
    item0 = Column(BigInteger)
    item1 = Column(BigInteger)
    item2 = Column(BigInteger)
    item3 = Column(BigInteger)
    item4 = Column(BigInteger)
    item5 = Column(BigInteger)
    item6 = Column(BigInteger)
    killingSprees = Column(BigInteger)
    kills = Column(BigInteger)
    largestCriticalStrike = Column(BigInteger)
    largestKillingSpree = Column(BigInteger)
    largestMultiKill = Column(BigInteger)
    magicDamageDealt = Column(BigInteger)
    magicDamageDealtToChampions = Column(BigInteger)
    magicDamageTaken = Column(BigInteger)
    minionsKilled = Column(BigInteger)
    neutralMinionsKilled = Column(BigInteger)
    neutralMinionsKilledEnemyJungle = Column(BigInteger)
    nodeCapture = Column(BigInteger)
    nodeCaptureAssist = Column(BigInteger)
    nodeNeutralize = Column(BigInteger)
    nodeNeutralizeAssist = Column(BigInteger)
    objectivePlayerScore = Column(BigInteger)
    pentaKills = Column(BigInteger)
    physicalDamageDealt = Column(BigInteger)
    physicalDamageDealtToChampions = Column(BigInteger)
    physicalDamageDealtTaken = Column(BigInteger)
    quadraKills = Column(BigInteger)
    sightWardsBoughtInGame = Column(BigInteger)
    teamObjective = Column(BigInteger)
    totalDamageDealt = Column(BigInteger)
    totalDamageDealtToChampions = Column(BigInteger)
    totalDamageTaken = Column(BigInteger)
    totalHeal = Column(BigInteger)
    totalPlayerScore = Column(BigInteger)
    totalScoreRank = Column(BigInteger)
    totalTimeCrowdControlDealt = Column(BigInteger)
    totalUnitsHealed = Column(BigInteger)
    towerKills = Column(BigInteger)
    tripleKills = Column(BigInteger)
    trueDamageDealt = Column(BigInteger)
    trueDamageDealtToChampions = Column(BigInteger)
    trueDamageTaken = Column(BigInteger)
    unrealKills = Column(BigInteger)
    visionWardsBoughtInGame = Column(BigInteger)
    wardsKilled = Column(BigInteger)
    wardsPlaced = Column(BigInteger)
    winner = Column(Boolean)
