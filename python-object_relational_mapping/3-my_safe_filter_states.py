#!/usr/bin/python3
"""
This module contains the safe_filter_states function.
"""
import MySQLdb
from sys import argv


def safe_filter_states():
    """
    filters state safely based on user input
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
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (argv[4],))

    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    safe_filter_states()
