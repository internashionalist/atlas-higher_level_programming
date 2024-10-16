#!/usr/bin/python3
"""
This module contains the print_first_state function.
"""

import sys
import MySQLdb
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def print_first_state():
    """
    lists all State objects from database hbtn_0e_6_usa
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()

    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    session.close()


if __name__ == "__main__":
    print_first_state()
