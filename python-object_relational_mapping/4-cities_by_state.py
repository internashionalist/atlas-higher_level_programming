#!/usr/bin/python3
"""
This module contains the cities_by_state function.
"""

import MySQLdb
from sys import argv


def cities_by_states():
    """
    lists all cities from database hbtn_0e_4_usa
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities \
                INNER JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id ASC"
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    cities_by_states()
