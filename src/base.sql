CREATE TABLE Installation{
numero int
nom varchar(100),
adresse varchar (100),
code_postal varchar (6),
ville varchar (50),
latitude decimal,
longitude decimal,
PRIMARY KEY (numero)
}

CREATE TABLE Equipement{
numero int,
nom varchar(50),
PRIMARY KEY (numero,nom),
FOREIGN KEY (numero) REFERENCES Installation(numero)
}

CREATE TABLE Activite{
numero int,
nom varchar(50),
PRIMARY KEY (numero,nom),
FOREIGN KEY (numero) REFERENCES Installation(numero)
}
