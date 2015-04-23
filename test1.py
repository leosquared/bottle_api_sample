import json, os
from bottle import route, run, static_file, request

pth_xml     = os.path.dirname(os.path.realpath(__file__)) + '/xml/'


@route('/')
def hello():
	return 'hello, world'

@route('/recipes/')
def recipes_list():
    paths = []
    ls = os.listdir(pth_xml)
    print ls
    for entry in ls:
    	if ".xml" == os.path.splittext(entry)[1]:
    		paths.append(entry)
    return {'success':True, "paths":paths}

@route('/recipes/<name>', method='GET')
def recipe_show( name=""):
    if name != '':
    	return static_file(name, pth_xml)
    else:
    	return { "success" : False, "error" : "show called without a filename" }

@route('/recipes/<name>', method='DELETE' )
def recipe_delete( name="Mystery Recipe" ):
    return { "success" : False, "error" : "delete not implemented yet" }

@route('/recipes/<name>', method='PUT')
def recipe_save( name='' ):
	input_xml = request.forms.get('xml')
	if name != '' and input_xml != '':
		with open(os.path.join(pth_xml, name+'.xml'), 'w') as write_file:
			write_file.write(input_xml)
		return {'success':True, 'path':name}
	else:
		return {'success':False, 'error':'no input file specified'}



run(host='localhost', port='8080', debug=True)