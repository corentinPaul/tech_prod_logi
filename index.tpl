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
			tab = {{!tab}} //connect the js variable to py variable
			act = {{!act}} //connect the js variable to py variable
			
			code_postal = {{!code_postal}}//
			num_act = {{!num_act}}//
		</script>
  </head>
  <body>
    <h1> Trouver une installation, un équipement ou une activité en pays de la loire </h1>
    <form method="get" action="/info">
		  <div id="radio">
			 <input type="radio" id="radio1" name="radio"><label onclick="code_choisie()" for="radio1">Ville/Code postal</label>
			 <input type="radio" id="radio2" name="radio"><label for="radio2" onclick="act_choisie()">Activité</label>
		  </div>

		<div id="choix_code">
		   Choisir un code postal</br>
		   <input class="input_texte" name="postal" type="text" id="autocomplete_postal"></input>
		</div>
		<div id="choix_act">
		   Choisir une activité </br>
		   <input class="input_texte" name="act" type="text" id="autocomplete_activite"></input>
		</div>

      <!--</br>
      veuillez selectionnner un équipement (exemple: terrain de basket) </br>

      <select id="select_equip">
      </select>


      </br>
      veuillez selectionner une installation <br>

      <select id="select_inst">
      </select>-->
      <input type="submit" value="soumettre" id="sub"></input>
    </form>
    
    
    
    <!-- CORENTIN  -->
    <h2>Résultats</h2>
    
    
    <!-- FIN CORENTIN  -->
  </body>
</html>
