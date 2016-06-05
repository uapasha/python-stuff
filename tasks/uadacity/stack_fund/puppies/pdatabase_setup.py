############# setup ###################
import sys

from sqlalchemy import Column, ForeignKey, Integer, String, DATE, Numeric

from sqlalchemy import create_engine

from sqlalchemy.orm import relationship

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

############# class ###################
class Shelter(Base):
	############# table ###################
	__tablename__ = 'shelter'
	############# mapping #################
	name = Column(String(80), nullable = False)
	address = Column(String(100))
	city = Column(String(40))
	state = Column(String(40))
	zipCode = Column (String(10))
	website = Column(String(100))
	max_capacity = Column(Integer)
	current_occupancy = Column(Integer)
	id = Column(Integer, primary_key = True)

############# class ###################
class Puppy(Base):
	############# table ###################
	__tablename__ = 'puppy'

	############# mapping #################
	id = Column(Integer, primary_key = True)
	name = Column(String(40), nullable = False)
	dateOfBirth = Column(DATE)
	gender = Column(String(20), nullable = False)
	weight = Column(Numeric(10))
	picture = Column(String)
	shelter_id = Column(Integer, ForeignKey('shelter.id'))
	shelter = relationship("Shelter")

	adopter_id = Column(Integer)
	
	adopters = relationship("Adopter")


class PuProfile(Base):
	__tablename__ = 'puprofile'
	############# mapping #################
	id = Column(Integer, ForeignKey('puppy.id'), primary_key = True)
	url = Column(String)
	description = Column(String)
	special_needs = Column(String)

	puppy = relationship(Puppy)


class Adopter(Base):
	__tablename__ = "adopters"

	############## mapping ################
	id = Column(Integer, primary_key = True)
	name = Column(String(80))
	adopted_puppy_id = Column(Integer, ForeignKey('puppy.id'), nullable = False)
	adopted_puppy = relationship(Puppy)
############# ending of setup #########
engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.create_all(engine)