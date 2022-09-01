import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    name = Column(String(150), nullable = False)
    password = Column(Integer, nullable = False)
    
class Character(Base):
    __tablename__= 'character'
    id = Column(Integer, primary_key = True)
    name = Column(String(150), nullable = False)
    image = Column(String(250), nullable = False)
    age = Column(String(5), nullable = False)
    height = Column(String(5), nullable = False)


class Planets(Base):
    __tablename__='planet' 
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable = False)
    image = Column(String(250), nullable = False)
    rotation_period = Column(String(7), nullable = False)
    orbital_period = Column(String(7), nullable = False)
    gravity = Column(String(5), nullable = False)
    terrain = Column(String(150), nullable = False)

class Favorites(Base):
    __tablename__='favorite'
    id = Column(Integer, primary_key = True)
    character_id = Column(Integer, ForeignKey("character.id"))
    character = relationship("Character")
    planet_id = Column(Integer, ForeignKey("planet.id"))
    planet = relationship("Planet")
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User")


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')