#!/usr/bin/python3
"""
Module that contains a script that deletes an Object whith
a name containing the letter a from the database hbtn_0e_6_usa
"""


import sqlalchemy
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = session()
    s = '%a%'
    states = session.query(State).filter(State.name.like(s))
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
