from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine("sqlite:///notes.db")

class Note(Base):
    __tablename__="notes"

    id = Column(Integer, primary_key=True)
    noteText = Column(String(5000))

def CreateDB():
    Base.metadata.create_all(engine)


def GetSession():
    DBSession = sessionmaker(bind=engine)
    return DBSession()