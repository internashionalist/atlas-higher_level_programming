#!/usr/bin/python3
"""
This module contains the get_state function.
"""
import sys
import MySQLdb
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def get_state():
    """
    prints State object with name passed as argument
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(
        State.name == sys.argv[4]).order_by(State.id)

    if state.count() == 0:
        print("Not found")
    else:
        print(state[0].id)

    session.close()


if __name__ == "__main__":
    get_state()
