<! DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8"/>
      <title>sport en pays de la loire</title>
      <link rel="stylesheet" type="text/css" href="static/style.css" media="screen" />
      <link rel="stylesheet" href="https://code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
  		<script src="https://code.jquery.com/jquery-1.10.2.js"></script>
  		<script src="https://code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
      <script src="static/script.js"></script>
      
      <script>
			tab = {{!tab}}
		</script>
  </head>
  <body>
    <h1> Trouver une installation, un équipement ou une activité en pays de la loire </h1>
    <form method="post" action="./../serveur/template.tpl">
    
    
      veuillez rentrer un code postal</br>
      <input type="text" id="autocomplete_postal"></input> </br>
      veuillez selectionner une activité </br>
      <select id="select_act">
		
      </select>
		
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
