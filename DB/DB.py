#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import csv

cr = csv.reader(open("./../src/Installation.csv","r"))
conn = sqlite3.connect('DataBase.db')

cursor = conn.cursor()
cursor.execute("""DROP TABLE IF EXISTS Installation""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS installation(
   numero_inst INTEGER PRIMARY KEY UNIQUE,
	nom_usuel_inst varchar(100),
	numero_voie INTEGER,
	nom_voie varchar (100),
	code_postal varchar (5),
	commune varchar (50),
	lieu_dit varchar(50)
)
""")

installations = []
for i,row in enumerate(cr):
	if i > 0:
		installations.append((row[1], row[0],row[6],row[7],row[4],row[2],row[5]))
	
cursor.executemany("""INSERT INTO Installation(numero_inst, nom_usuel_inst,numero_voie,nom_voie,code_postal,commune,lieu_dit) VALUES(?, ?, ?, ?, ?, ?, ?)""", installations)

conn.commit()

#cursor.execute("""SELECT nom_usuel_instal FROM installations""")
#rows = cursor.fetchall()
#for row in rows:
#    print('{0}'.format(row[0]))
