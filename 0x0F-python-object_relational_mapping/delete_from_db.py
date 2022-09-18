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
    state = session.query(State).filter_by(id=7).first()
    session.delete(state)
    print(str(state.name))
    session.commit()
    session.close()
