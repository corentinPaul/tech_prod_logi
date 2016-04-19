from libs.bottle import route, template, run, static_file


#@route('/<name>')
#def index(name):
#	return template('template', name=name)
@route('/')
def index():
	return template('index')
	
@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

run(host='localhost', port=8080)
