from libs.bottle import route, template, run, static_file, get
import sqlite3
import json


@get('/info')
def index():
    return '<b>Hello </b>!'

#@get('/info&<num>')
#def index(num):
#    return template('<b>Hello {{num}}</b>!',num=num)*/
    
@get('/info&postal=<postal>')
def index(postal):
    return template('<b>code postal = {{postal}} </b>!',postal=postal)

@get('/info&act=<act>')
def index(act):
    return template('<b>num act =  {{act}}</b>!',act=act)
    

@route('/')
def index():
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

	return template('index', tab=json.dumps(tab), act=json.dumps(act),num_act=0,code_postal=0)

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')


run(host='localhost', port=8080)
