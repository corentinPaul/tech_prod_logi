CREATE TABLE Installation{
numero_inst int, // numéro d Installation
nom_usel_inst varchar(100),// nom usuel
nom_de_voie varchar (100), //addres de l Installation
code_postal varchar (6), // code postal de la ville
commune varchar (50), // commune qui hebere l installation
lieu-dit varchar(50), // nom du lieu dit
PRIMARY KEY (numero_inst)
}

CREATE TABLE Equipement{
equipement_id int //numéro équipement,
nom_equip varchar(50), //nom de l équipement
numero_inst int, //numéro d installation
longitude decimal,
latitude decimal,
PRIMARY KEY (equipement_id,nom_equip),
FOREIGN KEY (numero_inst) REFERENCES Installation(numero_inst)
}

CREATE TABLE Activite{
act_code int,// numero d Activite
libv_acti varchar(100), // nom de l Activite
equipement_id varchar(50), // numero d Equipement
PRIMARY KEY (equipement_id,act_code),
FOREIGN KEY (equipement_id) REFERENCES Installation(equipement_id)
}
