#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('DataBase.db')

cursor = conn.cursor()
cursor.execute("""DROP TABLE IF EXISTS users""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     age INTERGER
)
""")


users = []
users.append(("olivier", 30))
users.append(("jean-louis", 90))
cursor.executemany("""INSERT INTO users(name, age) VALUES(?, ?)""", users)

conn.commit()

cursor.execute("""SELECT id, name, age FROM users""")
rows = cursor.fetchall()
for row in rows:
    print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))
