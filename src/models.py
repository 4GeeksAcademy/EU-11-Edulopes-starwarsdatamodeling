import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(length=12), nullable=False)
    favorites = Column(Integer, ForeignKey('favorites.id'))
   

# class Account(Base):
#     __tablename__ = 'account'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     user_id = Column(Integer, ForeignKey('user.id'))
#     id = Column(Integer, primary_key=True)
#     user_username = Column(String(250), nullable=False)
#     user_password = Column(String(length=12), nullable=False)
#     first_name = Column(String(250), nullable=False)
#     last_name = Column(String,(250), nullable=False)
#     email = Column(String(250), nullable=False)
#     user = relationship(User)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    characters = relationship('Characters')
    planets = relationship('Planets')
    vehicles = relationship('Vehicles')
    users = relationship('User')

class Characters(Base):
    __tablename__ = 'charactesrs'
    id = Column(Integer, primary_key=True)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birthyear = Column(String(250))
    gender = Column(String(250))
    favorites = Column(Integer, ForeignKey('favorites.id'))

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(Integer)
    population = Column(Integer)
    climate = Column(Integer)
    terrain = Column(String(250))
    surface_water = Column(String(250), nullable=True)
    created = Column(String(250))
    edited = Column(String(250))
    name = Column(String(250))
    favorites = Column(Integer, ForeignKey('favorites.id'))

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    model = Column(Integer)
    starship_class = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(String(250))
    length = Column(Integer)
    crew = Column(String(250))
    passengers = Column(String(250))
    hyperdrive_rating = Column(String(250))
    mglt = Column(String(250))
    cargo_capacity = Column(Integer)
    consumables = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))
    name = Column(String(250))
    favorites = Column(Integer, ForeignKey('favorites.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
