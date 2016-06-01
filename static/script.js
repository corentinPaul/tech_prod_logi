$( document ).ready(function() {

 	$( "#radio" ).buttonset();

  $(function() {

    $( "#radio" ).buttonset();
  });
  $("#choix_code").click();
  $("#sub").button();
	$("#autocomplete_postal").autocomplete({source: tab}); //that make an autocomplete for city and postal code
	$("#autocomplete_activite").autocomplete({source: act}); //that make an autocomplete for city and postal code

	check = false;
	$("#form").submit(function(event){
		var code_post = 0;
		var num_act = 0;
		var temp;
			event.preventDefault();
			if ($("#autocomplete_postal").val() != "")
			{
			//IL FAUT VERIFIER SIL Y A UN TIRET
				temp = $("#autocomplete_postal").val().split(" - ");
				code_post = temp[0];
			}
			if ($("#autocomplete_activite").val() != "")
			{
				temp = $("#autocomplete_activite").val().split(" - ");
				num_act = temp[0];
			}
			window.location.href ="http://localhost:8080/info&postal="+code_post+"&act="+num_act;
	});
	
	if (code_postal != 0 || num_acti !=0)
	{
		if (code_postal == -1 || num_acti == -1)
		{
			$("#resultats").html("<h2>Veuillez sélectionner une ville ou une activité valide</h2>");
		}
		else if (table.length == 0 && maps.length == 0)
		{
			$("#resultats").html("<h2>Aucun résultats trouvés</h2>");
		}
		else
		{
			if (nom_ville !="")
			{
				var tFootHead = "<tr><td>Activité</td><td>Installation</td><td>Adresse</td></tr>";
				var tBody = "";
				for (i = 0;i<table.length;i++)
				{
					tBody += "<tr>";
					tBody += "<td>"+table[i][1]+"</td>";
					tBody += "<td>"+table[i][2]+"</td>";
					tBody += "<td>"+table[i][3]+"</td>";
					tBody += "</tr>";
				}
				$("#tbody_info").html(tBody);
				$("#tfoot_info").html(tFootHead);
				$("#thead_info").html(tFootHead);
			}
			else
			{
				var tFootHead = "<tr><td>Installation</td><td>Adresse</td><td>Commune</td></tr>";
				var tBody = "";
				for (i = 0;i<table.length;i++)
				{
					tBody += "<tr>";
					tBody += "<td>"+table[i][1]+"</td>";
					tBody += "<td>"+table[i][2]+"</td>";
					tBody += "<td>"+table[i][3]+"</td>";
					tBody += "</tr>";
				}
				$("#tbody_info").html(tBody);
				$("#tfoot_info").html(tFootHead);
				$("#thead_info").html(tFootHead);
			}
			
			$("#resultats").animate({'opacity':'0'},0);
			$("#onglets").tabs();
			maps = new GMaps({
			  div: '#maps',
			  lat: -12.043333,
			  lng: -77.028333
			})
			
			setTimeout(function()
			{
				$("#onglet-1").css('width','');
				$("#li_2").click();
				$("#resultats").animate({'opacity':'1'},500);
				$('#table_resultats').DataTable();
			},1000);
		}
	}
	else
	{
		$("#resultats").remove();
	}



//CORENTIN
    $("#onglets").tabs();
     $('#test').DataTable();
     maps = new GMaps({
  div: '#onglet-1',
  lat: -12.043333,
  lng: -77.028333
})
    //fin CORENTIN
})

function code_choisie()
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

function act_choisie()
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

// CORENTIN



//FIN CORENTIN
