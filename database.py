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
    participantIdentities = relationship("ParticipantIdentity", single_parent=True,
                                         cascade="save-update, merge, delete, delete-orphan", backref="match")
    participants = relationship("Participant", single_parent=True, cascade="save-update, merge, delete, delete-orphan",
                                backref="match")
    platformId = Column(String)
    queueType = Column(String)
    region = Column(String)
    season = Column(String)
    teams = relationship("Team", single_parent=True, cascade="save-update, merge, delete, delete-orphan",
                         backref="match")
    timeline = relationship("Timeline", single_parent=True, cascade="save-update, merge, delete, delete-orphan",
                            backref="match")

# Set relation
class Participant(Base):
    __tablename__ = 'participant'

    id = Column(BigInteger, primary_key=True)
    matchId = Column(BigInteger, ForeignKey('match_detail.matchId'))
    championId = Column(Integer)
    highestAchievedSeasonTier = Column(String)
    masteries = relationship("Mastery", single_parent=True, cascade="save-update, merge, delete, delete-orphan",
                             backref="participant")
    participantId = Column(Integer)
    runes = relationship("Rune", single_parent=True, cascade="save-update, merge, delete, delete-orphan",
                         backref="participant")
    spell1Id = Column(Integer)
    spell2Id = Column(Integer)
    stats = relationship("ParticipantStats", single_parent=True, cascade="save-update, merge, delete, delete-orphan",
                         backref="participant")
    teamId = Column(Integer)
    timeline = relationship("ParticipantTimeline", single_parent=True,
                            cascade="save-update, merge, delete, delete-orphan", backref="participant")

# Add relations
class ParticipantIdentity(Base):
    __tablename__ = 'participant_identity'

    id = Column(BigInteger, primary_key=True)
    matchId = Column(BigInteger, ForeignKey('match_detail.matchId'))
    participantId = Column(Integer)


class Team(Base):
    __tablename__ = 'team'

    id = Column(BigInteger, primary_key=True)
    matchId = Column(BigInteger, ForeignKey('match_detail.matchId'))
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

    id = Column(BigInteger, primary_key=True)
    matchId = Column(BigInteger, ForeignKey('match_detail.matchId'))
    frameInterval = Column(BigInteger)


class Mastery(Base):
    __tablename__ = 'mastery'

    id = Column(BigInteger, primary_key=True)
    participantId = Column(BigInteger, ForeignKey('participant.id'))
    masteryId = Column(BigInteger)
    rank = Column(BigInteger)


class ParticipantStats(Base):
    __tablename__ = 'participant_stats'

    id = Column(BigInteger, primary_key=True)
    participantId = Column(BigInteger, ForeignKey('participant.id'))
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


class ParticpantTimeline(Base):
    __tablename__ = 'participant_timeline'

    id = Column(BigInteger, primary_key=True)
    participantId = Column(BigInteger, ForeignKey('participant.id'))
    lane = Column(String)
    role = Column(String)


class Rune(Base):
    __tablename__ = 'rune'

    id = Column(BigInteger, primary_key=True)
    participantId = Column(BigInteger, ForeignKey('participant.id'))
    rank = Column(BigInteger)
    runeId = Column(BigInteger)


class Player(Base):
    __tablename__ = 'player'

    matchHistoryUri = Column(String)
    profileIcon = Column(Integer)
    summonerId = Column(BigInteger)
    summonerName = Column(String)


class BannedChampion(Base):
    __tablename__ = 'banned_champion'

    championId = Column(Integer)
    pickTurn = Column(Integer)


class Frame(Base):
    __tablename__ = 'frame'

    timestamp = Column(BigInteger)


class ParticipantTimelineData(Base):
    __tablename__ = 'participant_timeline_data'

    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class Event(Base):
    __tablename__ = 'event'

    ascendedType = Column(String)
    buildingType = Column(String)
    creatorId = Column(Integer)
    eventType = Column(String)
    itemAfter = Column(Integer)
    itemBefore = Column(Integer)
    itemId = Column(Integer)
    killerId = Column(Integer)
    laneType = Column(String)
    levelUpType = Column(String)
    monsterType = Column(String)
    participantId = Column(Integer)
    pointCaptured = Column(String)
    skillSlot = Column(Integer)
    teamId = Column(Integer)
    timestamp = Column(BigInteger)
    towerType = Column(String)
    victimId = Column(Integer)
    wardType = Column(String)


class ParticipantFrame(Base):
    __tablename__ = 'participant_frame'

    currentGold = Column(Integer)
    dominionScore = Column(Integer)
    jungleMinionsKilled = Column(Integer)
    level = Column(Integer)
    minionsKilled = Column(Integer)
    participantId = Column(Integer)
    teamScore = Column(Integer)
    totalGold = Column(Integer)
    xp = Column(Integer)


class Position(Base):
    __tablename__ = 'position'

    x = Column(Integer)
    y = Column(Integer)
