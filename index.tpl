<! DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8"/>
      <title>sport en pays de la loire</title>
      <link rel="stylesheet" type="text/css" href="static/style.css" media="screen" />
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
      <script src="static/script.js"></script>
  </head>
  <body>
    <h1> Trouver une installation, un équipement ou une activité en pays de la loire </h1>
    <form method="post" action="./../serveur/template.tpl">
    
    
      veuillez rentrer un code postal</br>
      <input type="text"></input> </br>
      veuillez selectionner une activité </br>
      <select id="select_act">
		
      </select>

		<script>
		tab = [];
		var i = 0;
		<%import sqlite3

			conn = sqlite3.connect('static/sports_pdl.db')
			cursor = conn.cursor()
			cursor.execute("""SELECT DISTINCT code_postal FROM installation""")
			for x in cursor.fetchall():%>
				var val = {{x[0]}}
				tab[i] = val;
				i++;
			%end
		</script>
		
      </br>
      veuillez selectionnner un équipement (exemple: terrain de basket) </br>
      
      <select id="select_equip">
      </select>
      
      
      </br>
      veuillez selectionner une installation <br>
      
      <select id="select_inst">
      </select>
      
      </br>
      <input type="submit" value="soumettre" id="sub"></input>
    </form>
    <h2>Résultats</h2>
  </body>
</html>
