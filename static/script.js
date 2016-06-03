$( document ).ready(function() {

 	$( "#radio" ).buttonset();
	carteChargee=false;
  $(function() {

    $( "#radio" ).buttonset();
  });
  $("#choix_code").click();
  $("#sub").button();
	$("#autocomplete_postal").autocomplete({source: tab}); //that make an autocomplete for city and postal code -> corentin
	$("#autocomplete_activite").autocomplete({source: act}); //that make an autocomplete for city and postal code -> corentin

	check = false;
	$("#form").submit(function(event){//lors de l'envoit du formulaire
		var code_post = 0;
		var num_act = 0;
		var temp;
			event.preventDefault();//on annule l'effet du bouton par défaut.
			if ($("#autocomplete_postal").val() != "")//code postal choisi
			{
			//IL FAUT VERIFIER SIL Y A UN TIRET
				temp = $("#autocomplete_postal").val().split(" - ");
				code_post = temp[0];//on récupère les 5 premiers caractères qui doivent être le code postal
			}
			if ($("#autocomplete_activite").val() != "")//activite choisi
			{
				temp = $("#autocomplete_activite").val().split(" - ");
				num_act = temp[0];//on récupère les caractères avant le tiret qui sont le code de l'activite
			}
			window.location.href ="http://localhost:8080/info&postal="+code_post+"&act="+num_act;//on accède à cette adresse qui sera interprete par server.py pour renvoyer les données utiles.
	});
	
	if (code_postal != 0 || num_acti !=0)//cela veut dire que le server.py à renvoyer un code_postal ou un numéro d'activité donc le formulaire a été envoyé. On va donc traiter les données
	{
		$("#premier_plan").remove();//on enlève le premier plan qui est inutile
		if (code_postal == -1 || num_acti == -1)
		{
			$("#resultats").html("<h2>Veuillez sélectionner une ville ou une activité valide</h2>");//L'activite ou la ville n'a pas été selectionné dans la liste s'affichant et les premiers caractères ne contenait pas les bons codes.
		}
		else if (table.length == 0 && maps.length == 0)
		{
			$("#resultats").html("<h2>Aucun résultats trouvés</h2>");//le code était valide mais il n'y a eu aucun résultats.
		}
		else
		{
			$("#resultats").animate({'opacity':'0'},0);//on cache les résultats le temps de mettre en forme
				$("#onglets").tabs();
				map = new GMaps({//on crée la google map
				  div: '#maps',
				  lat: 47.218038,//coordonnée en dur de Nantes
				  lng: -1.555146
				})
				
			if (nom_ville !="")//une ville est retournée
			{
				var tFootHead = "<tr><td>Activité</td><td>Installation</td><td>Adresse</td></tr>";//on affiche les activités, les isntallations et l'adresse
				var tBody = "";
				for (i = 0;i<table.length;i++)
				{
					tBody += "<tr class='tr_table' onclick='afficherAdresse(\""+table[i][3]+"\","+i+")'>";
					tBody += "<td>"+table[i][2]+"</td>";
					tBody += "<td>"+table[i][1]+"</td>";
					tBody += "<td>"+table[i][3]+"</td>";
					tBody += "</tr>";
				}
				$("#tbody_info").html(tBody);
				$("#tfoot_info").html(tFootHead);
				$("#thead_info").html(tFootHead);
				
				$("#choix").html("Vous avez choisi la ville de <b>" + nom_ville + " "+ code_postal
									+"</b><br><b>"+table.length+"</b> résultats retournés");
			}
			else//une activité à été choisie
			{
				var tFootHead = "<tr><td>Installation</td><td>Adresse</td><td>Commune</td></tr>";//on affiche donc les isntallations, les adresses et la commune pour pouvoir trier par commune si on veut
				var tBody = "";
				for (i = 0;i<table.length;i++)
				{
					tBody += "<tr class='tr_table' onclick='afficherAdresse(\""+table[i][3]+"\","+i+")'>";
					tBody += "<td>"+table[i][1]+"</td>";
					tBody += "<td>"+table[i][3]+"</td>";
					tBody += "<td>"+table[i][2]+"</td>";
					tBody += "</tr>";
				}
				$("#tbody_info").html(tBody);
				$("#tfoot_info").html(tFootHead);
				$("#thead_info").html(tFootHead);
				
				$("#choix").html("Vous avez choisi l'activité<b> " + nom_act
								+"</b><br><b>"+table.length+"</b> résultats retournés");
			}
			listeforMarkers = [];
			for (j = 0;j<table.length;j++)
				{//pour chaque adresse on récupère les coordonnées grâce à la fonction Geocode qui donne les coordonnées via une adresse (l'adresse concaténée dans server.py)
					temp = table[j];
					ij = 0;
					GMaps.geocode({
					  address: table[j][3],
					  callback: function(results, status)//limité à 10 requêtes envoyées.Fonction callback asynchrone et résultats renvoyés dans le désordre.
					  {
						 //console.log("testj " + j);
						 
						 if (status == 'OK')
						 {
						 	//console.log(results);
						 	listeforMarkers.push([results[0],ij]);
						 }
						 ij++;
	  					}
					});
				}
			GMaps.geocode({
				  address: 'Nantes, France',
				  callback: function(results, status)
				  {
					 if (status == 'OK')
					 {
						var latlng = results[0].geometry.location;
						map.setCenter(latlng.lat(), latlng.lng());//On centre la carte sur Nantes
					 }
  					}
				});
			
			setTimeout(function()
			{
				$("#onglet-1").css('width','');//la carte sort du cadre sinon
				$("#li_2").click();//la carte a chargée donc on affiche le tableau
				$('#table_resultats').DataTable();//on met en forme le tableau avec le plugin dataTable
				$("#resultats").animate({'opacity':'1'},500);//on affiche les résultats maintenant qu'ils sont prêt
				$(window).scrollTop($("#choix").offset().top);//on scroll pour montrer les résultats
			},1000);
		}
	}
	else
	{
		$("#resultats").remove();//il n'y a pas de résultats donc on enlève le html de la page car inutile
	}

})

function code_choisie()//code postal choisi donc affiche la sélection du code postal
{
	$("#choix_code").css('display','block');
	$("#choix_act").css('display','none');
	$(".input_texte").val("");
	/*$("#choix_code").css('z-index','99999');
	$("#choix_code").animate({opacity :1},500);
	$("#choix_act").animate({opacity :0},500);
	setTimeout(function()
	{
		$(".input_texte").val("");
		$("#choix_act").css('z-index','1');
	},500);*/
}

function act_choisie()//activité choisi donc on affiche la selection de l'activité
{
	$("#choix_code").css('display','none');
	$("#choix_act").css('display','block');
	$(".input_texte").val("");
	/*$("#choix_act").css('z-index','0');
	$("#choix_code").animate({opacity :0},500);
	$("#choix_act").animate({opacity :1},500);
	setTimeout(function()
	{
		$(".input_texte").val("");
		$("#choix_code").css('z-index','1');
	},500);*/
}

function afficher_page()//on enleve le premier plan
{
	$("#premier_plan").fadeOut();
}

function chargerCarte()//on a cliqué sur l'onglet MAPS donc ajotue les markers à la maps grâce à la boucle Geocode précédente limité à 10
{
	if (!carteChargee)
	{
	
				console.log(listeforMarkers);
				console.log(table);
		if (nom_ville !="")
		{		
			for (f=0;f<listeforMarkers.length;f++)
			{
				//console.log(listeforMarkers[f]);
				latlng = listeforMarkers[f][0].geometry.location;
				//alert(latlng.lat());
				num = listeforMarkers[f][1];
				//console.log(num + " "+ table[num][3]);
				//num=(num-table.length)*-1;
				map.addMarker({
				  lat: latlng.lat(),
				  lng: latlng.lng(),
				  infoWindow: {
					  content: '<p><b>'+table[num][2]+"</b><br>"
					  					+table[num][1]+"<br>"
					  					+table[num][3]+'</p>'//quand on clique sur un marqueur on affiche les données de celui-ci.
					}
				});
			}
		}
		else
		{
			for (f=0;f<listeforMarkers.length;f++)
			{
				//console.log(listeforMarkers[f]);
				latlng = listeforMarkers[f][0].geometry.location;
				//alert(latlng.lat());
				map.addMarker({
				  lat: latlng.lat(),
				  lng: latlng.lng(),
				  infoWindow: {
					  content: '<p><b>'+table[listeforMarkers[f][1]][1]+"</b><br>"
					  					+table[listeforMarkers[f][1]][3]+'</p>'
					}
				});
			}
		}
		carteChargee=true;
	}
}

function afficherAdresse(adresse, i)//on affiche l'adresse quand on clique sur un tr de la table.
{
	map.setZoom(19);//zoom avant sur l'adresse
	if (nom_ville !="")
	{
		GMaps.geocode({
		  address: adresse,
		  callback: function(results, status)
		  {
			 if (status == 'OK')
			 {
				var latlng = results[0].geometry.location;
				map.setCenter(latlng.lat(), latlng.lng());
				map.addMarker({
					  lat: latlng.lat(),
					  lng: latlng.lng(),
					  infoWindow: {
						  content: '<p><b>'+table[i][2]+"</b><br>"
					  					+table[i][1]+"<br>"
					  					+table[i][3]+'</p>'
						}
					});
			 }
			}
		});
	}
	else
	{
		GMaps.geocode({
		  address: adresse,
		  callback: function(results, status)
		  {
			 if (status == 'OK')
			 {
				var latlng = results[0].geometry.location;
				map.setCenter(latlng.lat(), latlng.lng());
				map.addMarker({
					  lat: latlng.lat(),
					  lng: latlng.lng(),
					  infoWindow: {
						  content: '<p><b>'+table[i][1]+"</b><br>"
						  					+table[i][3]+'</p>'
						}
					});
			 }
			}
		});
	}
	$("#li_1").click();
	setTimeout(function()
	{
		map.zoomOut();//zoom arrière pour voir les alentours
		map.zoomOut();
	},1000);
}
// CORENTIN



//FIN CORENTIN
