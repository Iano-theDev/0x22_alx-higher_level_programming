#!/usr/bin/python3
"""
Module to query an exact state name from database
"""


import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = session()
    s = argv[4]
    state = session.query(State).filter(State.name.like(s)).first()
    if state is not None:
        print(str(state.id))
    else:
        print("Not found")
    session.close()
