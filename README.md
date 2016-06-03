# tech_prod_logi
this project is to create a web showing of "Pays de la Loire" sport installation with python script
____________________________________________________how to launch____________________________</br>
1 place you in the tech_prod_logi folder </br>
2 create database using python3  db/createdb.py </br>
3 launch server using python3 server.py command</br>
4 open a web browser and go to http://localhost:8080/ </br>
____________________________________________________contents_________________________________</br>

in main folder: </br>
db folder: contains the database and the script to create it </br>
index.tpl : the html web page </br>
libs folder: libs for the python server /!\ we don't garanty the good working of this project if you modified it /!\ </br>
README.md : a texte file with description of project how to launch it and other important information </br>
server.py: a python server who runs the App </br>
sports_pdl.db: a copy of the database but we advises you to download the 3 csv  file and put them in db/csv folder  to create the database and run createdb.py </br>
static folder: contains static file to have interraction with the web page such as a css or javascript files </br>
requete.txt: request to get result on the website

___________________________________________________sources____________________________________</br>
to get the csv files:</br>
activities:</br> http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-activites-des-fiches-equ/</br>
equipements:</br>
http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-fiches-equipements/</br>
installation:</br>
http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-fiches-installations/
