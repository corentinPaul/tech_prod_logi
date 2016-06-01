<! DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8"/>
      <title>sport en pays de la loire</title>
      <link rel="stylesheet" type="text/css" href="static/style.css" media="screen" />
      <link rel="stylesheet" href="https://code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
  		<script src="https://code.jquery.com/jquery-1.10.2.js"></script>
  		<script src="https://code.jquery.com/ui/1.11.4/jquery-ui.js"></script>

  		<link rel="stylesheet" href="http://cdn.datatables.net/1.10.11/css/jquery.dataTables.min.css">
		<script src="http://cdn.datatables.net/1.10.11/js/jquery.dataTables.min.js"></script>
 		<script type="text/javascript" src="http://maps.google.com/maps/api/js"></script>
		<script src="http://raw.githubusercontent.com/HPNeo/gmaps/master/gmaps.js"></script>

      <script src="static/script.js"></script>

      <script>
			tab = {{!tab}} //connect the js variable to py variable
			act = {{!act}} //connect the js variable to py variable


			code_postal = {{!code_postal}}//code_postal choisi si choisi
			num_acti = {{!num_act}}//numéro activité choisi si choisi

			maps = {{!maps}}//les coordonnées des installations pour maps
			table = {{!table}}//les infos sur les installations pour la table
<<<<<<< HEAD
			
			nom_ville = {{!ville}}
			nom_act = {{!activite}}
=======



			//code_postal = {{!code_postal}}//
			//num_act = {{!num_act}}//
>>>>>>> 2d1511882055c2adb7740a2b8b9cfd29b6c75a27
		</script>
  </head>
  <body>
    <div id="premier_plan">
    
    <p id="titre_main"> Bienvenue sur le site des activitées sportives en Pays de Loire
    </p>
    <input id="submit_main" type="submit" value="effectuer une recherche">
    </div>
    <h1> Trouver une installation, un équipement ou une activité en pays de la loire </h1>
    <form id="form">
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

    <div id="resultats">
			<div id="onglets">
				<ul>
				  <li><a href="#onglet-1" id="li_1">MAPS</a></li>
				  <li><a href="#onglet-2" id="li_2">TABLEAU</a></li>
				</ul>
				<div id="onglet-1">
					<div id="maps"></div>
				</div>
				<div id="onglet-2">
				  <table id="table_resultats">
				   <thead id="thead_info">

				   </thead>
				   <tfoot id="tfoot_info">

				   </tfoot>
				   <tbody id="tbody_info">

				   </tbody>

				  <table>
				</div>
			 </div>
		</div>




  </body>
</html>
