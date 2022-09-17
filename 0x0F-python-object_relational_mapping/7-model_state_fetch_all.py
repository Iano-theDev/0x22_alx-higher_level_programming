#!/usr/bin/python3
"""
script that lists all state objects from the database hbtn_0e_0_usa
"""


import sqlalchemy
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3], pool_pre_ping=True))
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
for state in session.query(State).order_by(State.id):
    print("{}: {}".format(state.id, state.name))
session.close()
