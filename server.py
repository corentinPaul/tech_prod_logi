from libs.bottle import route, template, run, static_file,get, post
import sqlite3
import json


@get('/info')
def index():
    return '<b>Hello machin</b>!'
    
@get('/info&<num>')
def index(num):
    return template('<b>Hello {{num}}</b>!',num=num)

@route('/select<post>')
def select(post):
	return post
	conn = sqlite3.connect('static/sports_pdl.db')# in order to have access to the database you must connect
	cursor = conn.cursor()
	cursor.execute("""SELECT lib_act FROM activite WHERE equipement_id = (SELECT equipement_id FROM equipement WHERE numero_inst =  (SELECT numero_inst FROM installation WHERE code_postal = """+post+""" ))""")
	for y in cursor2.fetchall():
		print(y[0])
	return template('select',select_act = json.dumps(select_act),post=post)

@route('/')
def index():
	conn = sqlite3.connect('static/sports_pdl.db')# in order to have access to the database you must connect
	cursor = conn.cursor()
	cursor.execute("""SELECT DISTINCT code_postal, commune FROM installation WHERE code_postal != '' AND commune != '' ORDER BY code_postal ASC""")
	#request that return the postal code and the name of the city
	tab = []
	temp_comm = ''
		
	for x in cursor.fetchall(): #separator for each row of the cursor
		if temp_comm == x[1] :
			temp_val = tab[-1]
			tab[tab.index(temp_val)] = '-- ' + x[1]+ ' --'
			tab.append(temp_val)
		temp_comm = x[1]
		tab.append(x[0]+" - "+x[1])

	#cursor.execute("""SELECT act_code, lib_act, equipement_id, code_postal FROM activite WHERE
	#code_postal = (SELECT code_postal FROM installation WHERE installation.numero_inst = (SELECT numero_inst FROM equipement WHERE equipement_id = activite.equipement_id))""")

	return template('index', tab=json.dumps(tab))

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')


run(host='localhost', port=8080)
