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
    bans = relationship("BannedChampion", single_parent=True,
                        cascade="save-update, merge, delete, delete-orphan", backref="team")
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
    frames = relationship("Frame", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="timeline")


class Mastery(Base):
    __tablename__ = 'mastery'

    id = Column(BigInteger, primary_key=True)
    participant_id = Column(BigInteger, ForeignKey('participant.id'))
    masteryId = Column(BigInteger)
    rank = Column(BigInteger)


class ParticipantStats(Base):
    __tablename__ = 'participant_stats'

    id = Column(BigInteger, primary_key=True)
    participant_id = Column(BigInteger, ForeignKey('participant.id'))
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


class ParticipantTimeline(Base):
    __tablename__ = 'participant_timeline'

    id = Column(BigInteger, primary_key=True)
    participant_id = Column(BigInteger, ForeignKey('participant.id'))
    ancientGolemAssistsPerMinCounts = relationship("AncientGolemAssistsPerMinCounts", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="participantTimeline")
    ancientGolemKillsPerMinCounts = relationship("AncientGolemKillsPerMinCounts", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="participantTimeline")
    assistedLaneDeathsPerMinDeltas = relationship("AssistedLaneDeathsPerMinDeltas", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="participantTimeline")
    assistedLaneKillsPerMinDeltas = relationship("AssistedLaneKillsPerMinDeltas", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="participantTimeline")
    baronAssistsPerMinCounts = relationship("BaronAssistsPerMinCounts", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="participantTimeline")
    baronKillsPerMinCounts = relationship("BaronKillsPerMinCounts", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="participantTimeline")
    creepsPerMinDeltas = relationship("CreepsPerMinDeltas", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="participantTimeline")
    csDiffPerMinDeltas = relationship("CsDiffPerMinDeltas", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="participantTimeline")
    damageTakenDiffPerMinDeltas = relationship("DamageTakenDiffPerMinDeltas", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="participantTimeline")
    damageTakenPerMinDeltas = relationship("DamageTakenPerMinDeltas", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="participantTimeline")
    dragonAssistsPerMinCounts = relationship("DragonAssistsPerMinCounts", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="participantTimeline")
    dragonKillsPerMinCounts = relationship("DragonKillsPerMinCounts", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="participantTimeline")
    elderLizardAssistsPerMinCounts = relationship("ElderLizardAssistsPerMinCounts", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="participantTimeline")
    elderLizardKillsPerMinCounts = relationship("ElderLizardKillsPerMinCounts", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="participantTimeline")
    goldPerMinDeltas = relationship("GoldPerMinDeltas", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="participantTimeline")
    inhibitorAssistsPerMinCounts = relationship("InhibitorAssistsPerMinCounts", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="participantTimeline")
    inhibitorKillsPerMinCounts = relationship("InhibitorKillsPerMinCounts", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="participantTimeline")
    lane = Column(String)
    role = Column(String)
    towerAssistsPerMinCounts = relationship("TowerAssistsPerMinCounts", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="participantTimeline")
    towerKillsPerMinCounts = relationship("TowerKillsPerMinCounts", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="participantTimeline")
    towerKillsPerMinDeltas = relationship("TowerKillsPerMinDeltas", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="participantTimeline")
    vilemawAssistsPerMinCounts = relationship("VilemawAssistsPerMinCounts", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="participantTimeline")
    vilemawKillsPerMinCounts = relationship("VilemawKillsPerMinCounts", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="participantTimeline")
    wardsPerMinDeltas = relationship("WardsPerMinDeltas", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="participantTimeline")
    xpDiffPerMinDeltas = relationship("XpDiffPerMinDeltas", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="participantTimeline")
    xpPerMinDeltas = relationship("XpPerMinDeltas", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="participantTimeline")


class Rune(Base):
    __tablename__ = 'rune'

    id = Column(BigInteger, primary_key=True)
    participant_id = Column(BigInteger, ForeignKey('participant.id'))
    rank = Column(BigInteger)
    runeId = Column(BigInteger)


class Player(Base):
    __tablename__ = 'player'

    id = Column(BigInteger, primary_key=True)
    matchHistoryUri = Column(String)
    profileIcon = Column(Integer)
    summonerId = Column(BigInteger)
    summonerName = Column(String)


class BannedChampion(Base):
    __tablename__ = 'banned_champion'

    id = Column(BigInteger, primary_key=True)
    team_id = Column(BigInteger, ForeignKey('team.id'))
    championId = Column(Integer)
    pickTurn = Column(Integer)


class Frame(Base):
    __tablename__ = 'frame'

    id = Column(BigInteger, primary_key=True)
    timeline_id = Column(BigInteger, ForeignKey('timeline.id'))
    events = relationship("Event", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="frame")
    participantFrames = relationship("ParticipantFrame", single_parent=True,
                          cascade="save-update, merge, delete, delete-orphan", backref="frame")
    timestamp = Column(BigInteger)


class AncientGolemAssistsPerMinCounts(Base):
    __tablename__ = 'ancient_golem_assists_per_min_counts'

    id = Column(BigInteger, primary_key=True)
    participantTimeline_id = Column(BigInteger, ForeignKey('participant_timeline.id'))
    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class AncientGolemKillsPerMinCounts(Base):
    __tablename__ = 'ancient_golem_kills_per_min_counts'

    id = Column(BigInteger, primary_key=True)
    participantTimeline_id = Column(BigInteger, ForeignKey('participant_timeline.id'))
    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class AssistedLaneDeathsPerMinDeltas(Base):
    __tablename__ = 'assisted_lane_deaths_per_min_deltas'

    id = Column(BigInteger, primary_key=True)
    participantTimeline_id = Column(BigInteger, ForeignKey('participant_timeline.id'))
    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class AssistedLaneKillsPerMinDeltas(Base):
    __tablename__ = 'assisted_lane_kills_per_min_deltas'

    id = Column(BigInteger, primary_key=True)
    participantTimeline_id = Column(BigInteger, ForeignKey('participant_timeline.id'))
    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class BaronAssistsPerMinCounts(Base):
    __tablename__ = 'baron_assists_per_min_counts'

    id = Column(BigInteger, primary_key=True)
    participantTimeline_id = Column(BigInteger, ForeignKey('participant_timeline.id'))
    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class BaronKillsPerMinCounts(Base):
    __tablename__ = 'baron_kills_per_min_counts'

    id = Column(BigInteger, primary_key=True)
    participantTimeline_id = Column(BigInteger, ForeignKey('participant_timeline.id'))
    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class CreepsPerMinDeltas(Base):
    __tablename__ = 'creeps_per_min_deltas'

    id = Column(BigInteger, primary_key=True)
    participantTimeline_id = Column(BigInteger, ForeignKey('participant_timeline.id'))
    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class CsDiffPerMinDeltas(Base):
    __tablename__ = 'cs_diff_per_min_deltas'

    id = Column(BigInteger, primary_key=True)
    participantTimeline_id = Column(BigInteger, ForeignKey('participant_timeline.id'))
    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class DamageTakenDiffPerMinDeltas(Base):
    __tablename__ = 'damage_taken_diff_per_min_deltas'

    id = Column(BigInteger, primary_key=True)
    participantTimeline_id = Column(BigInteger, ForeignKey('participant_timeline.id'))
    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class DamageTakenPerMinDeltas(Base):
    __tablename__ = 'damage_taken_per_min_deltas'

    id = Column(BigInteger, primary_key=True)
    participantTimeline_id = Column(BigInteger, ForeignKey('participant_timeline.id'))
    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class DragonAssistsPerMinCounts(Base):
    __tablename__ = 'dragon_assists_per_min_counts'

    id = Column(BigInteger, primary_key=True)
    participantTimeline_id = Column(BigInteger, ForeignKey('participant_timeline.id'))
    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class DragonKillsPerMinCounts(Base):
    __tablename__ = 'dragon_kills_per_min_counts'

    id = Column(BigInteger, primary_key=True)
    participantTimeline_id = Column(BigInteger, ForeignKey('participant_timeline.id'))
    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class ElderLizardAssistsPerMinCounts(Base):
    __tablename__ = 'elder_lizard_assists_per_min_counts'

    id = Column(BigInteger, primary_key=True)
    participantTimeline_id = Column(BigInteger, ForeignKey('participant_timeline.id'))
    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class ElderLizardKillsPerMinCounts(Base):
    __tablename__ = 'elder_lizard_kills_per_min_counts'

    id = Column(BigInteger, primary_key=True)
    participantTimeline_id = Column(BigInteger, ForeignKey('participant_timeline.id'))
    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class GoldPerMinDeltas(Base):
    __tablename__ = 'gold_per_min_deltas'

    id = Column(BigInteger, primary_key=True)
    participantTimeline_id = Column(BigInteger, ForeignKey('participant_timeline.id'))
    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class InhibitorAssistsPerMinCounts(Base):
    __tablename__ = 'inhibitor_assists_per_min_counts'

    id = Column(BigInteger, primary_key=True)
    participantTimeline_id = Column(BigInteger, ForeignKey('participant_timeline.id'))
    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class InhibitorKillsPerMinCounts(Base):
    __tablename__ = 'inhibitor_kills_per_min_counts'

    id = Column(BigInteger, primary_key=True)
    participantTimeline_id = Column(BigInteger, ForeignKey('participant_timeline.id'))
    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class TowerAssistsPerMinCounts(Base):
    __tablename__ = 'tower_assists_per_min_counts'

    id = Column(BigInteger, primary_key=True)
    participantTimeline_id = Column(BigInteger, ForeignKey('participant_timeline.id'))
    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class TowerKillsPerMinCounts(Base):
    __tablename__ = 'tower_kills_per_min_counts'

    id = Column(BigInteger, primary_key=True)
    participantTimeline_id = Column(BigInteger, ForeignKey('participant_timeline.id'))
    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class TowerKillsPerMinDeltas(Base):
    __tablename__ = 'tower_kills_per_min_deltas'

    id = Column(BigInteger, primary_key=True)
    participantTimeline_id = Column(BigInteger, ForeignKey('participant_timeline.id'))
    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class VilemawAssistsPerMinCounts(Base):
    __tablename__ = 'vilemaw_assists_per_min_counts'

    id = Column(BigInteger, primary_key=True)
    participantTimeline_id = Column(BigInteger, ForeignKey('participant_timeline.id'))
    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class VilemawKillsPerMinCounts(Base):
    __tablename__ = 'vilemaw_kills_per_min_counts'

    id = Column(BigInteger, primary_key=True)
    participantTimeline_id = Column(BigInteger, ForeignKey('participant_timeline.id'))
    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class WardsPerMinDeltas(Base):
    __tablename__ = 'wards_per_min_deltas'

    id = Column(BigInteger, primary_key=True)
    participantTimeline_id = Column(BigInteger, ForeignKey('participant_timeline.id'))
    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class XpDiffPerMinDeltas(Base):
    __tablename__ = 'xp_diff_per_min_deltas'

    id = Column(BigInteger, primary_key=True)
    participantTimeline_id = Column(BigInteger, ForeignKey('participant_timeline.id'))
    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class XpPerMinDeltas(Base):
    __tablename__ = 'xp_per_min_deltas'

    id = Column(BigInteger, primary_key=True)
    participantTimeline_id = Column(BigInteger, ForeignKey('participant_timeline.id'))
    tenToTwenty = Column(Float)
    thirtyToEnd = Column(Float)
    twentyToThirty = Column(Float)
    zeroToTen = Column(Float)


class Event(Base):
    __tablename__ = 'event'

    id = Column(BigInteger, primary_key=True)
    frame_id = Column(BigInteger, ForeignKey('frame.id'))
    ascendedType = Column(String)
    assistingParticipantIds = relationship("AssistingParticipantIds", single_parent=True,
                                           cascade="save-update, merge, delete, delete-orphan", backref="event")
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
    position = relationship("PositionEvent", single_parent=True,
                            cascade="save-update, merge, delete, delete-orphan", backref="event")
    skillSlot = Column(Integer)
    teamId = Column(Integer)
    timestamp = Column(BigInteger)
    towerType = Column(String)
    victimId = Column(Integer)
    wardType = Column(String)


class AssistingParticipantIds(Base):
    __tablename__ = 'assisting_participant_ids'
    id = Column(BigInteger, primary_key=True)
    event_id = Column(BigInteger, ForeignKey('event.id'))
    participantId = Column(Integer)


class ParticipantFrame(Base):
    __tablename__ = 'participant_frame'

    id = Column(BigInteger, primary_key=True)
    frame_id = Column(BigInteger, ForeignKey('frame.id'))
    currentGold = Column(Integer)
    dominionScore = Column(Integer)
    jungleMinionsKilled = Column(Integer)
    level = Column(Integer)
    minionsKilled = Column(Integer)
    participantId = Column(Integer)
    position = relationship("PositionParticipantFrame", single_parent=True,
                            cascade="save-update, merge, delete, delete-orphan", backref="participantFrame")
    teamScore = Column(Integer)
    totalGold = Column(Integer)
    xp = Column(Integer)


class PositionEvent(Base):
    __tablename__ = 'position_event'

    id = Column(BigInteger, primary_key=True)
    event_id = Column(BigInteger, ForeignKey('event.id'))
    x = Column(Integer)
    y = Column(Integer)


class PositionParticipantFrame(Base):
    __tablename__ = 'position_participant_frame'

    id = Column(BigInteger, primary_key=True)
    participantFrame_id = Column(BigInteger, ForeignKey('participant_frame.id'))
    x = Column(Integer)
    y = Column(Integer)
