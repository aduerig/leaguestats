from filler import Filler
from database import *
from sqlalchemy.orm import joinedload_all
import time

filler = Filler()

cs_winners = filler.session.query(CreepsPerMinDeltas).all()
filler.session.commit()

counter = 0
overall = 0
sum_zero_to_ten = 0
now = time.time()

# Index participantStats on participant_id, speeds everything up by a ton
for x in cs_winners:
    if not x.tenToTwenty:
        overall += 1
        continue
    if x.tenToTwenty >= 5:
        # Winner is 6.778857173748496, loser is 6.479495600446164
        # at 20 loser is 7.022837881219919, winner is 7.544212165017214
        if x.participantTimeline.participant.stats[0].winner:
            counter += 1
            sum_zero_to_ten += x.tenToTwenty
    overall += 1
    if (overall % 100) == 0:
        print(time.time() - now)
        now = time.time()

print(sum_zero_to_ten / counter)
