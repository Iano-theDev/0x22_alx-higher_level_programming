#!/usr/bin/python3
"""
Contains scripts that lists all city objects from the database
hbtn_0e_14_usa
"""


import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = session()
    cities = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id).all()
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
