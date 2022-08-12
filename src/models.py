import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    surname=Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)


class Address(Base):
    __tablename__ = 'foto'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_foto = Column(Integer, ForeignKey('person.id'))
    foto_name = Column(String(250))
    foto_description = Column(String(250))
    foto_location = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
   




    class Address(Base):
      __tablename__ = 'reel'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_reel = Column(Integer, primary_key=True)
    location_reel = Column(String(250))
    description_reel = Column(String(250))
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

    