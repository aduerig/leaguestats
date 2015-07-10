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
        match = self.session.query(MatchDetail).filter(MatchDetail.matchId == json_obj['flat']['matchId'])

        # Fill participantIdentities
        tmp_arr = []
        for x in json_obj['participantIdentities']:
            tmp_arr.append(ParticipantIdentity(**x['flat']))
        match.participantIdentities = tmp_arr

        # Fill participants
        tmp_arr = []
        for x in json_obj['participants']:
            tmp_arr.append(Participant(**x['flat']))
        match.participants = tmp_arr

        # Fill teams
        tmp_arr = []
        for x in json_obj['teams']:
            tmp_arr.append(Team(**x['flat']))
        match.teams = tmp_arr

        # Fill timeline
        tmp_arr = []
        for x in json_obj['timeline']:
            tmp_arr.append(Timeline(**x['flat']))
        match.timeline = tmp_arr
        self.session.commit()


# filler = Filler()
#
# filler.helloWorld()
