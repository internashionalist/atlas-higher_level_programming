#!/usr/bin/python3
"""
This module contains the filter_cities function.
"""
import MySQLdb
from sys import argv


def filter_cities():
    """
    takes state name as argument and lists all cities of that state
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
        "SELECT cities.name FROM cities INNER JOIN states ON \
                cities.state_id = states.id WHERE states.name = %s \
                ORDER BY cities.id ASC", (argv[4],)
    )

    print(", ".join([row[0] for row in cur.fetchall()]))

    cur.close()
    db.close()


if __name__ == "__main__":
    filter_cities()
