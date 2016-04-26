from libs.bottle import route, template, run, static_file
import sqlite3
import json


#@route('/<name>')
#def index(name):
#	return template('template', name=name)
@route('/')
def index():
	conn = sqlite3.connect('static/sports_pdl.db')# in order to have access to the database you must connect
	cursor = conn.cursor()
	cursor.execute("""SELECT DISTINCT code_postal, commune FROM installation WHERE code_postal != '' AND commune != '' ORDER BY code_postal ASC""")
	#request that return the postal code and the name of the city
	tab = []

	for x in cursor.fetchall(): #separator for each row of the cursor
		tab.append(x[0]+" - "+x[1])

	return template('index', tab=json.dumps(tab))

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')


run(host='localhost', port=8080)
