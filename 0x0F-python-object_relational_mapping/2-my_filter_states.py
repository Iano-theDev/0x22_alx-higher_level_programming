#!/usr/bin/python3
"""
fiter according to argument given
"""


import MySQLdb
from sqlite3 import Cursor
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
        else:
            print("the state {:s} is not in our database".format(argv[4]))
        cursor.close()
        db.close()
