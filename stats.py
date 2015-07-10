class GetStats:
    def __init__(self, jsonobj):
        self.jsonobj = jsonobj

    # Returns only with the data that isn't nested
    def returnMatchDetailFlat(self):
        newdict = {}
        for key in self.jsonobj:
            if((key != 'participantIdentities') & (key != 'participants')  & (key != 'teams') & (key != 'timeline')):
                newdict[key] = self.jsonobj[key]
        return newdict

    # Returns with the nested objects in the dictionary
    def returnMatchDetail(self):
        newdict = {}
        newdict['flat'] = self.returnMatchDetailFlat()
        for key in self.jsonobj:
            if key == 'participants':
                nestarrp = []
                for p in self.jsonobj['participants']:
                    nestarrp.append(self.returnParticipant(p))
                newdict['participants'] = nestarrp
            if key == 'participantIdentities':
                nestarrp = []
                for p in self.jsonobj['participantIdentities']:
                    nestarrp.append(self.returnParticipantIdentity(p))
                newdict['participantIdentities'] = nestarrp
            if key == 'teams':
                nestarrp = []
                for p in self.jsonobj['teams']:
                    nestarrp.append(self.returnTeam(p))
                newdict['teams'] = nestarrp
            if key == 'timeline':
                newdict['timeline'] = self.returnTimeline(self.jsonobj)
        return newdict

    def returnParticipantFlat(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            if((key != 'masteries') & (key != 'runes') & (key != 'stats') & (key != 'timeline') ):
                newdict[key] = jsonobj[key]
        return newdict

    def returnParticipant(self, jsonobj):
        newdict = {}
        newdict['flat'] = self.returnParticipantFlat(jsonobj)
        for key in jsonobj:
            if key == 'masteries':
                nestarrp = []
                for p in jsonobj['masteries']:
                    nestarrp.append(self.returnMastery(p))
                newdict['masteries'] = nestarrp
            if key == 'runes':
                nestarrp = []
                for p in jsonobj['runes']:
                    nestarrp.append(self.returnRune(p))
                newdict['runes'] = nestarrp
            if key == 'stats':
                nestdict = {}
                nestdict['flat'] = jsonobj['stats']
                newdict['stats'] = nestdict
            if key == 'timeline':
                newdict['timeline'] = self.returnParticipantTimeline(jsonobj)
        return newdict

    def returnParticipantIdentityFlat(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            if((key != 'player')):
                newdict[key] = jsonobj[key]
        return newdict

    def returnParticipantIdentity(self, jsonobj):
        newdict = {}
        newdict['flat'] = self.returnParticipantIdentityFlat(jsonobj)
        for key in jsonobj:
            if key == 'player':
                newdict[key] = self.returnPlayer(jsonobj['player'])
        return newdict

    def returnPlayerFlat(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            newdict[key] = jsonobj[key]
        return newdict

    def returnPlayer(self, jsonobj):  # has no nests
        newdict = {}
        newdict['flat'] = self.returnPlayerFlat(jsonobj)
        return newdict

    def returnMasteryFlat(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            newdict[key] = jsonobj[key]
        return newdict

    def returnMastery(self, jsonobj):  # has no nests
        newdict = {}
        newdict['flat'] = self.returnMasteryFlat(jsonobj)
        return newdict

    def returnRuneFlat(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            newdict[key] = jsonobj[key]
        return newdict

    def returnRune(self, jsonobj):  # has no nests
        newdict = {}
        newdict['flat'] = self.returnRuneFlat(jsonobj)
        return newdict

    def returnParticipantTimelineFlat(self, jsonobj):
        newdict = {}
        for key in jsonobj['timeline']:
            if((key == 'lane') | (key == 'role')):
                newdict[key] = jsonobj['timeline'][key]
        return newdict

    def returnParticipantTimeline(self, jsonobj):
        newdict = {}
        newdict['flat'] = self.returnParticipantTimelineFlat(jsonobj)
        nestarrp = []
        for p in jsonobj['timeline']:
            nestdict = {}
            if((p != 'lane') & (p != 'role')):
                nestdict[p] = jsonobj['timeline'][p]
                nestarrp.append(nestdict)
        newdict['ParticipantTimelineData'] = nestarrp
        return newdict

    def returnTeamFlat(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            if((key != 'bans')):
                newdict[key] = jsonobj[key]
        return newdict

    def returnTeam(self, jsonobj):
        newdict = {}
        newdict['flat'] = self.returnTeamFlat(jsonobj)
        nestarrp = []
        for key in jsonobj:
            if key == 'bans':
                nestarrp = []
                for p in jsonobj['bans']:
                    nestarrp.append(self.returnBannedChampion(p))
                newdict['bans'] = nestarrp
        return newdict

    def returnBannedChampionFlat(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            newdict[key] = jsonobj[key]
        return newdict

    def returnBannedChampion(self, jsonobj):  # has no nests
        newdict = {}
        newdict['flat'] = self.returnBannedChampionFlat(jsonobj)
        return newdict

    def returnTimelineFlat(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            if key == 'frameInterval':
                newdict[key] = jsonobj[key]
        return newdict

    def returnTimeline(self, jsonobj):
        newdict = {}
        newdict['flat'] = self.returnTimelineFlat(jsonobj['timeline'])
        nestdict = {}
        nestarrp = []
        for key in jsonobj['timeline']:
            if key == 'frames':
                for p in jsonobj['timeline'][key]:
                    nestdict[key] = self.returnFrame(p)
                    nestarrp.append(nestdict)
        newdict['timeline'] = nestarrp
        return newdict

    def returnFrameFlat(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            if((key != 'participantFrames') & (key != 'events')):
                newdict[key] = jsonobj[key]
        return newdict

    def returnFrame(self, jsonobj):
        newdict = {}
        newdict['flat'] = self.returnFrameFlat(jsonobj)
        for key in jsonobj:
            if key == 'events':
                nestarrp = []
                for p in jsonobj['events']:
                    nestdict = {}
                    nestdict[key] = self.returnEvent(p)
                    nestarrp.append(nestdict)
                newdict['events'] = nestarrp
            if key == 'participantFrames':
                nestarrp = []
                for p in jsonobj['participantFrames']:
                    nestarrp.append(self.returnParticipantFrame(jsonobj['participantFrames']))
                newdict['participantFrames'] = nestarrp
        return newdict

    def returnEventFlat(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            if((key != 'position') & (key != 'assistingParticipantIds')):
                newdict[key] = jsonobj[key]
        return newdict

    def returnEvent(self, jsonobj):
        newdict = {}
        newdict['flat'] = self.returnEventFlat(jsonobj)
        for key in jsonobj:
            if key == 'position':
                newdict['position'] = self.returnPosition(jsonobj['position'])
            if key == 'assistingParticipantIds':  # fix
                newdict['assistingParticipantIds'] = self.returnAssistingParticipantId(jsonobj['assistingParticipantIds'])
        return newdict

    def returnPositionFlat(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            newdict[key] = jsonobj[key]
        return newdict

    def returnPosition(self, jsonobj):  # has no nests
        newdict = {}
        newdict['flat'] = self.returnFrameFlat(jsonobj)
        return newdict

    def returnAssistingParticipantIdFlat(self, jsonobj):
        pass
        # newdict = {}
        # print(jsonobj)
        # for key in jsonobj:
        #     newdict[key] = jsonobj[key]
        # return newdict

    def returnAssistingParticipantId(self, jsonobj):  # has no nests
        # newdict = {}
        # newdict['flat'] = self.returnAssistingParticipantIdFlat(jsonobj)
        return jsonobj

    def returnParticipantFrameFlat(self, jsonobj):
        newdict = {}
        for key in jsonobj:
            if((key != 'position')):
                newdict[key] = jsonobj[key]
        return newdict

    def returnParticipantFrame(self, jsonobj): # there may be something wrong in this function
        newdict = {}
        newdict['flat'] = self.returnParticipantFrameFlat(jsonobj)
        for key in jsonobj:
            if key == 'position':
                newdict['position'] = self.returnPosition(jsonobj['position'])
        return newdict
