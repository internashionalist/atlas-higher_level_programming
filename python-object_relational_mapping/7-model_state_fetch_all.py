#!/usr/bin/python3
"""
This module contains the list_states function.
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def list_states():
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

    for item in session.query(State).order_by(State.id):
        print("{}: {}".format(item.id, item.name))

    session.close()


if __name__ == "__main__":
    list_states()
