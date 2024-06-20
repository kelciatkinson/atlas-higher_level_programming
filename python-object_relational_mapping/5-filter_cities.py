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

    query = """SELECT cities.name FROM states JOIN cities
    ON cities.state_id = states.id WHERE states.name = %s"""
    cur.execute(query, (argv[4],))

    rows = cur.fetchall()

    cities = []

    for row in rows:
        cities.append(row[0])

    if cities:
        print(", ".join(cities))

    cur.close()
    db.close()

