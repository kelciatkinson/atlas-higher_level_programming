#!/usr/bin/python3
"""Here is some documentation"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """This is so the file will not be executed when imported"""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
    )

    cur = db.cursor()

    cur.execute("SELECT id, name"
                "FROM states WHERE name = '{}'".format(argv[4]))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
