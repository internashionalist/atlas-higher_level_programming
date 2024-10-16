#!/usr/bin/python3
"""
This module contains the print_cities function.
"""
import sys
import MySQLdb
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City


def print_cities():
    """
    prints all City objects from database hbtn_0e_14_usa
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).filter(
        City.state_id == State.id).all()

    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()


if __name__ == "__main__":
    print_cities()
