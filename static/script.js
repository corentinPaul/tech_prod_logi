$( document ).ready(function() {
  $(function() {
    $( "#radio" ).buttonset();
  });
  $("#choix_code").click();
  $("#sub").button();
	$("#autocomplete_postal").autocomplete({source: tab}); //that make an autocomplete for city and postal code
	$("#autocomplete_activite").autocomplete({source: act}); //that make an autocomplete for city and postal code
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
