CREATE TABLE Installation{
numero_inst int, -- numéro d Installation col B 2
nom_usuel_inst varchar(100),-- nom usuel  col A 1
numero_voie int, -- numero de voie  G 7
nom_de_voie varchar (100), --addres de l Installation  col H 8
code_postal varchar (6), -- code postal de la ville  col E 5
commune varchar (50), -- commune qui hebere l installation C 3
lieu_dit varchar(50), -- nom du lieu dit F 6
PRIMARY KEY (numero_inst)
}

CREATE TABLE Equipement{
equipement_id int --numéro équipement, E 5
nom_equip varchar(50), --nom de l équipement D 4
numero_inst int, --numéro d installation C 3
longitude decimal, --FY 181
latitude decimal, --FZ 182
PRIMARY KEY (equipement_id,nom_equip),
FOREIGN KEY (numero_inst) REFERENCES Installation(numero_inst)
}

CREATE TABLE Activite{
act_code int,-- numero d Activite  E 5
libv_acti varchar(100), -- nom de l Activite F 6
equipement_id varchar(50), -- numero d Equipement C 3
PRIMARY KEY (equipement_id,act_code),
FOREIGN KEY (equipement_id) REFERENCES Installation(equipement_id)
}
