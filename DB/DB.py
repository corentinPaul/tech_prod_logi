#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import csv

conn = sqlite3.connect('DataBase.db')

# INSTALLATION

cr = csv.reader(open("./../src/Installation.csv","r"))

cursor = conn.cursor()
cursor.execute("""DROP TABLE IF EXISTS installation""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS installation(
   numero_inst INTEGER PRIMARY KEY,
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
	
cursor.executemany("""INSERT INTO installation(numero_inst, nom_usuel_inst,numero_voie,nom_voie,code_postal,commune,lieu_dit) VALUES(?, ?, ?, ?, ?, ?, ?)""", installations)

conn.commit()

# EQUIPEMENT

cr = csv.reader(open("./../src/Equipement.csv","r"))

cursor = conn.cursor()
cursor.execute("""DROP TABLE IF EXISTS equipement""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS equipement(
   equipement_id INTEGER,
	nom_equip varchar(50),
	numero_inst INTEGER,
	longitude DECIMAL,
	latitude DECIMAL,
	PRIMARY KEY (equipement_id,nom_equip),
	FOREIGN KEY (numero_inst) REFERENCES installation(numero_inst)
)
""")

equipements = []
for i,row in enumerate(cr):
	if i > 0:
		equipements.append((row[4], row[3],row[2],row[180],row[181]))
	
cursor.executemany("""INSERT INTO equipement(equipement_id,nom_equip,numero_inst,longitude,latitude) VALUES(?, ?, ?, ?, ?)""", equipements)

conn.commit()

# ACTIVITE

cr = csv.reader(open("./../src/Activite.csv","r"))

cursor = conn.cursor()
cursor.execute("""DROP TABLE IF EXISTS activite""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS activite(
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
   act_code INTEGER,
	lib_act varchar(100),
	equipement_id varchar(50),
	FOREIGN KEY (equipement_id) REFERENCES Installation(equipement_id)
)
""")

activites = []
for i,row in enumerate(cr):
	if i > 0:
		activites.append((row[4], row[5],row[2]))
	
cursor.executemany("""INSERT INTO activite(act_code,lib_act,equipement_id) VALUES(?, ?, ?)""", activites)

conn.commit()

#cursor.execute("""SELECT nom_usuel_instal FROM installations""")
#rows = cursor.fetchall()
#for row in rows:
#    print('{0}'.format(row[0]))
