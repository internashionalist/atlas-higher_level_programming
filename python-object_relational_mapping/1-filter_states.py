#!/usr/bin/python3
"""
This module contains the list_N_states function.
"""

import MySQLdb
import sys


def listNStates():
    """
    lists all states from database hbtn_0e_0_usa
    where state name starts with 'N'
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%'")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    listNStates()
