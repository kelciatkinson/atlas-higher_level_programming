#!/usr/bin/python3
"""Here is documentation"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """Does not execute if imported"""
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).get(2)

    if state:
        state.name = "New Mexico"
        session.commit()
    else:
        print("State with id = 2 not found")

    session.close()
