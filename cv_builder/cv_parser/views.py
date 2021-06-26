#from django.http import HttpResponse
from django.shortcuts import render
import json
from motionless import CenterMap
from urllib import request as req
import hashlib
import sys
import os
import logging
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from cv_latex import template
# Create your views here.

logger = logging.getLogger(__name__)

def index(request,lang="FR"):
	#template = loader.get_template('cv_parser/index.html')
	language="Français"
	language_code="fr"
	languages={ 'language':'English' , 'code':'us' , 'link':'EN' }
	if lang=="FR":
		with open("cv_parser/fr.json",'r') as config:
			json_config=json.loads(config.read())
			config.close()
	elif lang=="EN":
		language="English"
		languages={ 'language':'Français' , 'code':'fr' ,'link':'FR' }
		language_code="us"
		with open("cv_parser/en.json",'r') as config:
			json_config=json.loads(config.read())
			config.close()
	else:
		with open("cv_parser/fr.json",'r') as config:
			json_config=json.loads(config.read())
			config.close()
	#with open("cv_parser/cache.json","r") as cache_file:
	#	json_cache=json.loads(cache_file.read())
	#	cache_file.close()
	#hash_of_adress = json_config["contact"]["adress"].encode("utf-8")
	#hash_of_adress = hashlib.md5(hash_of_adress).hexdigest()

	#if json_cache["adress"] != hash_of_adress:

	cmap = CenterMap(address=json_config["contact"]["adress"],zoom=15, key="AIzaSyCKM9tkv_Rc9fMhuwLhwNwvW8C9Y6hNuNg")
	requ = req.Request(cmap.generate_url())
	pic = req.urlopen(requ)

	filePath = 'cv_parser/static/cv_parser/images/static_map.png'
	with open(filePath, 'wb') as localFile:
		localFile.write(pic.read())
		#json_cache["adress"] = hash_of_adress
		#with open("cv_parser/cache.json","w") as cache_file:
		#	json.dump(json_cache, cache_file)
		#	cache_file.close()

	
	#hash_of_config = json.dumps(json_config, sort_keys = True).encode("utf-8")
	#hash_of_config = hashlib.md5(hash_of_config).hexdigest()
	#logger.info(json_cache[lang.lower()+"_pdf_hash"])
	#logger.info(hash_of_config)
	#if json_cache[lang.lower()+"_pdf_hash"] != hash_of_config:
	template.create_template(json_config)
		#logger.info("new json")
		#json_cache[lang.lower()+"_pdf_hash"] = hash_of_config
		#with open("cv_parser/cache.json","w") as cache_file:
		#	json.dump(json_cache, cache_file)
		#	cache_file.close()

		# urllib.urlretrieve(self.url, filePath)
		
	return render(request, 'cv_parser/index.html', { 'config' : json_config  , 'language' : language , 'language_code' : language_code , 'languages': languages })

