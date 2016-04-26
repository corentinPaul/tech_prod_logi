# tech_prod_logi
this project is to create a web showing of "Pays de la Loire" sport installation with python script
____________________________________________________how to launch_______________________________________________________________
1 create database by launching createdb.py
2 launch server using python3 server.py command
3 open a web browser and go to http://localhost:8080/
____________________________________________________contents___________________________________________________________________
in main folder:
db folder: contains the database and the script to create it
index.tpl : the html web page
libs folder: libs for the python server /!\ we don't garanty the good working of this project if you modified it
README.md : a texte file with description of project how to launch it and other important information
server.py: a python server who runs the App
sports_pdl.db: a copy of the database but we advises you to download the 3 csv file to create the database and run createdb.py
static folder: contains static file to have interraction with the web page such as a css or javascript files

___________________________________________________sources_____________________________________________________________________
to get the csv files:
activities: http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-activites-des-fiches-equ/
equipements:
http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-fiches-equipements/
installation:
http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-fiches-installations/
