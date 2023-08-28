import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    climate = Column(String(250))
    created = Column(String(250))
    diameter = Column(String(250))
    gravity = Column(String(250))
    orbital_period = Column(String(250))
    population = Column(String(250))
    residents = Column(String(250))
    rotation_period = Column(String(250))
    surface_water = Column(String(250))
    terrain = Column(String(250))
    url = Column(String(250))

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    birth_year = Column(String(250))
    eye_color = Column(String(250))
    gender = Column(String(250))
    hair_color = Column(String(250))
    height = Column(String(250))
    homeworld = Column(String(250))
    mass = Column(String(250))
    skin_color = Column(String(250))
    species = Column(String(250))
    vehicles = Column(String(250))
    url = Column(String(250))

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))
    crew = Column(String(250))
    length = Column(String(250))
    manufacturer = Column(String(250))
    max_atmosphering_speed = Column(String(250))
    model = Column(String(250))
    passengers = Column(String(250))
    pilots = Column(String(250))
    url = Column(String(250))

class Starships(Base):
    __tablename__ = 'starships'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    MGLT = Column(String(250))
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))
    hyperdrive_rating = Column(String(250))
    length = Column(String(250))
    max_atmosphering_speed = Column(String(250))
    model = Column(String(250))
    passengers = Column(String(250))
    pilots = Column(String(250))
    manufacturer = Column(String(250))
    starship_class = Column(String(250))
    url = Column(String(250))

class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    starships_id = Column(Integer, ForeignKey('starships.id'))
    usuario = relationship(Usuario)
    planets = relationship(Planets)
    characters = relationship(Characters)
    vehicles = relationship(Vehicles)
    starships = relationship(Starships)
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')




#  person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)
