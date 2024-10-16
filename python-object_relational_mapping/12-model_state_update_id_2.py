#!/usr/bin/python3
"""
This module contains the change_state_name function.
"""
import sys
import MySQLdb
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def change_state_name():
    """
    changes the name of a State object
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()

    session.close()


if __name__ == "__main__":
    change_state_name()
