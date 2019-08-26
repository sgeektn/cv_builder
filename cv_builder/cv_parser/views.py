#from django.http import HttpResponse
from django.shortcuts import render
import json
from motionless import CenterMap
from urllib import request as req
import hashlib
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from cv_latex import template
# Create your views here.
def index(request,lang="FR"):
	#template = loader.get_template('cv_parser/index.html')
	if lang=="FR":
		with open("cv_parser/fr.json",'r') as config:
			json_config=json.loads(config.read())
			config.close()
	else:
		with open("cv_parser/fr.json",'r') as config:
			json_config=json.loads(config.read())
			config.close()
	with open("cv_parser/cache.json","r") as cache_file:
		json_cache=json.loads(cache_file.read())
		cache_file.close()

	hash_of_adress = json_config["contact"]["adress"].encode("utf-8")
	hash_of_adress = hashlib.md5(hash_of_adress).hexdigest()

	if json_cache["adress"] != hash_of_adress:
		cmap = CenterMap(address=json_config["contact"]["adress"],zoom=15, key="AIzaSyCKM9tkv_Rc9fMhuwLhwNwvW8C9Y6hNuNg=")
		requ = req.Request(cmap.generate_url())
		pic = req.urlopen(requ)
		filePath = 'cv_parser/static/cv_parser/images/static_map.png'
		with open(filePath, 'wb') as localFile:
			localFile.write(pic.read())
		json_cache["adress"] = hash_of_adress
		with open("cv_parser/cache.json","w") as cache_file:
			json.dump(json_cache, cache_file)
			cache_file.close()

	hash_of_config = json.dumps(json_config, sort_keys = True).encode("utf-8")
	hash_of_config = hashlib.md5(hash_of_config).hexdigest()

	if json_cache["pdf_hash"] != hash_of_config:
		template.create_template(json_config)
		
		json_cache["pdf_hash"] = hash_of_config
		with open("cv_parser/cache.json","w") as cache_file:
			json.dump(json_cache, cache_file)
			cache_file.close()

		# urllib.urlretrieve(self.url, filePath)
		
	return render(request, 'cv_parser/index.html', { 'config' : json_config })

