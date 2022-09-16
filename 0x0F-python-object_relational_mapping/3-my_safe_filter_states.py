#!/usr/bin/python3
"""filter states by user input & also safe from SQL injections"""


from sqlite3 import Cursor
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE {:s} ORDER BY id ASC", argv[4],)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()