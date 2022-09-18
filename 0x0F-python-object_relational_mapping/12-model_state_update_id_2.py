#!/usr/bin/python3
"""
Module contains script to change the name of a state object from a database
"""


import sqlalchemy
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = session()
    state = session.query(State).filter_by(id=2).first()
    state.name = 'New Mexico'
    session.commit()
    session.close()
