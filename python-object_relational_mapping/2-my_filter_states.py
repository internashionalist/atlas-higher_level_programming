#!/usr/bin/python3
"""
This module contains the search_states function.
"""

import MySQLdb
import sys


def search_states():
    """
    filters state based on user input
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE BINARY name LIKE '{}' ORDER BY id"
        .format(sys.argv[4]))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    search_states()
