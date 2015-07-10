from database import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *


class Filler:
    def __init__(self):
        self.engine = create_engine("sqlite:///test.db")
        Base.metadata.create_all(self.engine, checkfirst=True)

    def helloWorld(self):
        print("heyyo")

filler = Filler()

filler.helloWorld()