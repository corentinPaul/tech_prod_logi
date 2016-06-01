from libs.bottle import route, template, run, static_file, get
import sqlite3
import json


@get('/info')
def index():
    return '<b>Hello </b>!'

#@get('/info&<num>')
#def index(num):
#    return template('<b>Hello {{num}}</b>!',num=num)
    
@get('/info&postal=<postal>&act=<num_act>')
def index(postal,num_act):
	conn = sqlite3.connect('static/sports_pdl.db')# in order to have access to the database you must connect
	
	ville="''"
	activite="''"
	maps = []
	table = []
	#return template('<b>code postal = {{postal}} et <b>num act =  {{act}}</b>!</b>!',postal=postal, num_act = num_act)
	
	#REQUETES RECUP DONNEEE
	
	if(postal != 0):
		cursor3 = conn.cursor()
		cursor3.execute("""SELECT lib_act, numero_voie, nom_voie, lieu_dit, commune, nom_usuel_inst, longitude, latitude FROM installation i, equipement e, activite a WHERE i.numero_inst=e.numero_inst AND e.equipement_id=a.equipement_id AND code_postal ="""+postal+""" GROUP BY lib_act, numero_voie, nom_voie, lieu_dit, commune, nom_usuel_inst""")
		i=0
		for x in cursor3.fetchall(): #separator for each row of the cursor
			temp = [i,x[0],x[5],str(x[1])+" "+x[2]+" "+x[3]+" "+str(postal)+" "+x[4]]
			table.append(temp)
			temp = [i,x[6],x[7]]
			maps.append(temp)
			i = i+1
		
		cursor31 = conn.cursor()
		cursor31.execute("""SELECT commune FROM installation WHERE code_postal = """+postal+""" LIMIT 1""")

		for x in cursor31.fetchall(): #separator for each row of the cursor
			ville = "'"+x[0]+"'"
		
		
	if(num_act != 0):
		cursor4 = conn.cursor()
		cursor4.execute("""SELECT numero_voie, nom_voie, lieu_dit,code_postal, commune, nom_usuel_inst, longitude, latitude FROM installation i, equipement e, activite a WHERE i.numero_inst=e.numero_inst AND e.equipement_id=a.equipement_id AND  act_code="""+num_act+""" GROUP BY numero_voie, nom_voie,lieu_dit, code_postal, commune, nom_usuel_inst""")
		i = 0
		for x in cursor4.fetchall(): #separator for each row of the cursor
			temp = [i,x[5],str(x[0])+" "+x[1]+" "+x[2]+" "+str(x[3])+" "+x[4],x[4]]
			table.append(temp)
			temp = [i,x[6],x[7]]
			maps.append(temp)
			i = i+1
		
		cursor41 = conn.cursor()
		cursor41.execute("""SELECT lib_act FROM activite WHERE act_code="""+num_act+""" LIMIT 1""")

		for x in cursor41.fetchall(): #separator for each row of the cursor
			activite = "'"+x[0]+"'"
	
	#FIN REQUETES
	
	cursor = conn.cursor()
	cursor.execute("""SELECT DISTINCT code_postal, commune FROM installation WHERE code_postal != '' AND commune != '' ORDER BY code_postal ASC""")
	#request that return the postal code and the name of the city
	tab = []

	for x in cursor.fetchall(): #separator for each row of the cursor
		tab.append(x[0]+" - "+x[1])
	
	cursor2 = conn.cursor()
	cursor2.execute("""SELECT DISTINCT act_code, lib_act FROM activite ORDER BY act_code ASC""")
	#request that return the postal code and the name of the city
	act = []

	for y in cursor2.fetchall(): #separator for each row of the cursor
		act.append(str(y[0])+" - "+y[1])

	return template('index', tab=json.dumps(tab), act=json.dumps(act),num_act=num_act,code_postal=postal,table=json.dumps(table),maps=json.dumps(maps),ville=ville,activite=activite)

#@get('/info&act=<act>')
#def index(act):
#    return template('<b>num act =  {{act}}</b>!',act=act)
    

@route('/')
def index():
	ville="''"
	activite="''"
	maps = []
	table = []
	conn = sqlite3.connect('static/sports_pdl.db')# in order to have access to the database you must connect
	cursor = conn.cursor()
	cursor.execute("""SELECT DISTINCT code_postal, commune FROM installation WHERE code_postal != '' AND commune != '' ORDER BY code_postal ASC""")
	#request that return the postal code and the name of the city
	tab = []

	for x in cursor.fetchall(): #separator for each row of the cursor
		tab.append(x[0]+" - "+x[1])
	
	cursor2 = conn.cursor()
	cursor2.execute("""SELECT DISTINCT act_code, lib_act FROM activite ORDER BY act_code ASC""")
	#request that return the postal code and the name of the city
	act = []

	for y in cursor2.fetchall(): #separator for each row of the cursor
		act.append(str(y[0])+" - "+y[1])

	return template('index', tab=json.dumps(tab), act=json.dumps(act),num_act=0,code_postal=0,table=json.dumps(table),maps=json.dumps(maps),ville=ville,activite=activite)

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')


run(host='localhost', port=8080)
