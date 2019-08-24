#from django.http import HttpResponse
from django.shortcuts import render
import json
# Create your views here.
def index(request,lang="FR"):
	#template = loader.get_template('cv_parser/index.html')
	#if lang=="FR":
	with open("cv_parser/fr.json",'r') as config:
		json_config=json.loads(config.read())
		config.close()
	return render(request, 'cv_parser/index.html', { 'config' : json_config })

	