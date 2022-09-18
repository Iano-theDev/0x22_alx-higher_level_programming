#!/usr/bin/python3
"""
Module to insert a state into states Database
"""


import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, update
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = session()
    new_state = State(name='Louisiana')
    session.add(new_state)
    state = session.query(State).filter_by(name='Louisiana').first()
    print(str(state.id))
    session.commit()
    session.close()
