from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pdatabase_setup import Base, Puppy, Shelter

engine = create_engine ('sqlite:///puppyshelter.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Ex 1
puppies_alph = session.query(Puppy.name).order_by(Puppy.name)
for i in puppies_alph:
	print i.name

# Ex 2
import datetime
today = datetime.date.today()
edge_date = today - datetime.timedelta(days = 180)
x
ex2 = session.query(Puppy)\
			.filter(Puppy.dateOfBirth>edge_date)\
			.order_by(Puppy.dateOfBirth)


# ex 3
ex3 = session.query(Puppy.name, Puppy.weight).order_by(Puppy.weight)[:10]

# ex 4 
ex4 = session.query(Shelter.name.label('shelter'), \
					Puppy.name, Puppy.shelter_id, 
					Shelter.id)\
				.filter(Shelter.id == Puppy.shelter_id)\
				.order_by(Shelter.name)


