#!/usr/bin/python3
"""
This module contains the delete_a function.
"""
import sys
import MySQLdb
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def delete_a():
    """
    deletes State objects with 'a' in name
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like("%a%")).all()

    for state in states:
        session.delete(state)
    session.commit()

    session.close()


if __name__ == "__main__":
    delete_a()
