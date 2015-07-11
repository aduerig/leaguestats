from database import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *


class Filler:
    def __init__(self):
        self.engine = create_engine("sqlite:///test.db")
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        Base.metadata.create_all(self.engine, checkfirst=True)

    def add_match(self, json_obj):
        self.session.add(MatchDetail(**json_obj['flat']))
        match = self.session.query(MatchDetail).filter(MatchDetail.matchId == json_obj['flat']['matchId']).first()

        # ##########MatchDetail
        # Fill participantIdentities
        tmp_arr = []
        for x in json_obj['participantIdentities']:
            tmp_arr.append(ParticipantIdentity(**x['flat']))
        match.participantIdentities = tmp_arr

        # Fills all participant data
        match.participants = self.fill_participants(json_obj['participants'])

        # Fills match timeline data, has to be sent as array
        # match.timeline = [Timeline(**json_obj['timeline']['flat'])]
        match.timeline = self.fill_timeline(json_obj['timeline'])

        # Fill teams
        match.teams = self.fill_teams(json_obj['teams'])
        # ##########

        # Commit changes
        self.session.commit()

    def fill_teams(self, team_json):
        tmp_arr = []
        for x in team_json:
            x['flat']['bans'] = self.get_bans(x['bans'])
            tmp_arr.append(Team(**x['flat']))
        return tmp_arr

    @staticmethod
    def get_bans(bans_json):
        tmp_arr = []
        for x in bans_json:
            tmp_arr.append(BannedChampion(**x['flat']))
        return tmp_arr

    # Fill all participants
    def fill_participants(self, part_json):
        tmp_arr = []
        for x in part_json:
            x['flat']['masteries'] = self.get_masteries_arr(x['masteries'])
            x['flat']['runes'] = self.get_runes_arr(x['runes'])
            x['flat']['stats'] = [ParticipantStats(**x['stats']['flat'])]
            x['flat']['timeline'] = self.get_part_timeline(x['timeline'])

            tmp_arr.append(Participant(**x['flat']))
        return tmp_arr

    def fill_timeline(self, timeline_json):
        timeline_json['flat']['frames'] = self.get_frames(timeline_json['frames'])
        return [Timeline(**timeline_json['flat'])]

    def get_frames(self, frame_json):
        tmp_arr = []
        for x in frame_json:
            # x['flat']['participantFrames'] = self.get_part_frames(x['participantFrames'])
            if 'events' in x:
                x['flat']['events'] = self.get_events(x['events'])
            tmp_arr.append(Frame(**x['flat']))
        return tmp_arr

    @staticmethod
    def get_part_frames(part_frame_json):
        tmp_arr = []
        for x in part_frame_json:
            x['flat']['position'] = [PositionParticipantFrame(**x['position']['flat'])]

            tmp_arr.append(ParticipantFrame(**x['flat']))
        return tmp_arr

    def get_events(self, events_json):
        tmp_arr = []
        for x in events_json:
            if 'position' in x:
                x['flat']['position'] = [PositionEvent(**x['position']['flat'])]
            if 'assistingParticipantIds' in x:
                x['flat']['assistingParticipantIds'] = self.get_assisting_participant_ids(x['assistingParticipantIds'])

            tmp_arr.append(Event(**x['flat']))
        return tmp_arr

    @staticmethod
    def get_assisting_participant_ids(part_arr):
        tmp_arr = []
        for x in part_arr:
            tmp_arr.append(AssistingParticipantIds(participantId=x))
        return tmp_arr

    @staticmethod
    def get_part_timeline(timeline_part_json):
        t_json = timeline_part_json
        # Must return participantTimeline as an array [...]
        t_keys = list(timeline_part_json)
        t_keys.remove('flat')
        for x in t_keys:
            t_class = eval(x)
            y = (x[0].lower()) + (x[1:])
            t_json['flat'][y] = [t_class(**t_json[x]['flat'])]
        return [ParticipantTimeline(**t_json['flat'])]

    @staticmethod
    def get_masteries_arr(mast_json):
        tmp_arr = []
        for x in mast_json:
            tmp_arr.append(Mastery(**x['flat']))
        return tmp_arr

    @staticmethod
    def get_runes_arr(runes_json):
        tmp_arr = []
        for x in runes_json:
            tmp_arr.append(Rune(**x['flat']))
        return tmp_arr

    @staticmethod
    def get_part_stats_arr(stats_json):
        tmp_arr = []
        for x in stats_json:
            tmp_arr.append(ParticipantStats(**x['flat']))
        return tmp_arr

# filler = Filler()
#
# filler.helloWorld()
