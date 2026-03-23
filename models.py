from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Integer, Float, String

Base = declarative_base()

class Player(Base):
    __tablename__ = 'player'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    avg_pts = Column(Float)
    avg_assists = Column(Float)
    avg_reb = Column(Float)
    team_id = Column(Integer, ForeignKey('team.id'))

class Team(Base):
    __tablename__ = 'team'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)


