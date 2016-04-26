from libs.bottle import route, template, run, static_file, get
import sqlite3
import json


@get('/info')
def index():
    return '<b>Hello </b>!'
    
@get('/info&<num>')
def index(num):
    return template('<b>Hello {{num}}</b>!',num=num)
    
@route('/')
def index():
	conn = sqlite3.connect('static/sports_pdl.db')
	cursor = conn.cursor()
	cursor.execute("""SELECT DISTINCT code_postal, commune FROM installation WHERE code_postal != '' AND commune != '' ORDER BY code_postal ASC""")
	tab = []
	
	for x in cursor.fetchall():
		tab.append(x[0]+" - "+x[1])

	return template('index', tab=json.dumps(tab))
	
@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')


run(host='localhost', port=8080)
