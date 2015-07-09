class GetStats():
    def returnMatchDetail(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            if((key != 'participantIdentities') & (key != 'participants')  & (key != 'teams') & (key != 'timeline')):
                newdict[key] = jsonobj[key]
        return newdict

    def returnParticipant(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            if((key != 'masteries') & (key != 'runes')  & (key != 'stats') & (key != 'timeline')):
                newdict[key] = jsonobj[key]
        return newdict

    def returnParticipantIdentity(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            if((key != 'player')):
                newdict[key] = jsonobj[key]
        return newdict

    def returnTeam(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            if((key != 'bans')):
                newdict[key] = jsonobj[key]
        return newdict

    def returnTimeline(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            if((key != 'frames')):
                newdict[key] = jsonobj[key]
        return newdict

    def returnMastery(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            newdict[key] = jsonobj[key]
        return newdict

    def returnParticipantStats(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            newdict[key] = jsonobj[key]
        return newdict

    def returnParticipantTimeline(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            if((key == 'lane') | (key == 'role')):
                newdict[key] = jsonobj[key]
        return newdict

    def returnRune(jsonobj):
        newdict = {}
        for key in jsonobj:
            newdict[key] = jsonobj[key]
        return newdict

    def returnPlayer(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            newdict[key] = jsonobj[key]
        return newdict

    def returnBannedChampion(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            newdict[key] = jsonobj[key]
        return newdict

    def returnFrame(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            if((key != 'participantFrames') & (key != 'events')):
                newdict[key] = jsonobj[key]
        return newdict

    def returnParticipantTimelineData(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            newdict[key] = jsonobj[key]
        return newdict

    def returnEvent(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            if((key != 'position') & (key != 'assistingParticipantIds')):
                newdict[key] = jsonobj[key]
        return newdict

    def returnParticipantFrame(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            if((key != 'position')):
                newdict[key] = jsonobj[key]
        return newdict

    def returnPosition(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            newdict[key] = jsonobj[key]
        return newdict

    def returnAssistingParticipantIds(self, listint):
        newdict = {}
        for key in listint:
            newdict[str(key)] = key
        return newdict



    def returnEventList(self, jsonobj):
        arr = []
        for x in jsonobj['timeline']['frames']:
            if 'events' in x:
                for j in x['events']:
                    arr.append(self.returnEvent(j))
        return arr

    def returnParticipantList(self, jsonobj):
        arr = []
        for x in jsonobj['participants']:
            arr.append(self.returnParticipant(x))
        return arr

    def returnParticipantIdentityList(self, jsonobj):
        arr = []
        for x in jsonobj['participantIdentities']:
            arr.append(self.returnParticipantIdentity(x))
        return arr

    def returnTeamList(self, jsonobj):
        arr = []
        for x in jsonobj['teams']:
            arr.append(self.returnTeam(x))
        return arr

    def returnMasteryList(self, jsonobj):
        arr = []
        for x in jsonobj['participants']:
            for j in x['masteries']:
                arr.append(self.returnMastery(j))
        return arr

    def returnParticipantStatsList(self, jsonobj):
        arr = []
        for x in jsonobj['participants']:
            arr.append(self.returnParticipantStats(x['stats']))
        return arr

    def returnParticipantTimelineList(self, jsonobj):
        arr = []
        for x in jsonobj['participants']:
            arr.append(self.returnParticipantTimeline(x['timeline']))
        return arr

    def returnRuneList(self, jsonobj):
        arr = []
        for x in jsonobj['participants']:
            for j in x['runes']:
                arr.append(self.returnRune(j))
        return arr

    def returnPlayerList(self, jsonobj):
        arr = []
        for x in jsonobj['participantIdentities']:
            arr.append(self.returnPlayer(x['player']))
        return arr

    def returnBannedChampionList(self, jsonobj):
        arr = []
        for x in jsonobj['teams']:
            for j in x['bans']:
                arr.append(self.returnBannedChampion(j))
        return arr

    def returnFrameList(self, jsonobj): # there may be something wrong in this function
        arr = []
        for x in jsonobj['timeline']['frames']:
            arr.append(self.returnFrame(x))
        return arr

    def returnParticipantTimelineDataList(self, jsonobj): # there may be something wrong in this function
        arr = []
        for x in jsonobj['participants']:
            for j in x['timeline']:
                if((j != 'role') & (j != 'lane')):
                    arr.append(self.returnParticipantTimelineData(x))
        return arr

    def returnParticipantFrameList(self, jsonobj): # there may be something wrong in this function
        arr = []
        for x in jsonobj['timeline']['frames']:
            if 'participantFrames' in x:
                for j in range(1, 10):
                    arr.append(self.returnParticipantFrame(x['participantFrames'][str(j)]))
        return arr

    def returnPositionList(self, jsonobj):
        arr = []
        for x in jsonobj['timeline']['frames']:
            if 'participantFrames' in x:
                for j in range(1, 10):
                    arr.append(self.returnPosition(x['participantFrames'][str(j)]))
        return arr