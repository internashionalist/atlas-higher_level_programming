#!/usr/bin/python3
"""
This module contains the states_with_a function.
"""
import sys
import MySQLdb
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def states_with_a():
    """
    lists all State objects from database hbtn_0e_6_usa
    containing the letter 'a'
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    for item in session.query(State).filter(State.name.like("%a%")).order_by(State.id):
        print("{}: {}".format(item.id, item.name))

    session.close()


if __name__ == "__main__":
    states_with_a()
