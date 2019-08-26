import json
import os


def create_template(config):
	with open(os.path.dirname(os.path.realpath(__file__))+"/template_auto.tex","w") as template:
		if config["lang"].lower()=="fr":
			template.write("\\documentclass[letterpaper]{twentysecondcv_fr}\n")
		else:
			template.write("\\documentclass[letterpaper]{twentysecondcv_en}\n")
		template.write("\\usepackage[utf8]{inputenc}\n")

		template.write("\\profilepic{image.jpg} % Profile picture\n")
		template.write("\\cvname{"+config["general"]["name"].upper()+"} % Your name\n")
		template.write("\\cvjobtitle{\hspace{1.2cm}"+config["general"]["title"]+"}  % Job title/career\n")
		template.write("\\cvdate{"+config["general"]["date_of_birth"]+" "+config["general"]["place_of_birth"]+"} % Date of birth\n") 
		template.write("\\cvaddress{")
		i=0
		for adress_words in config["contact"]["adress"].split(" "):
			template.write(adress_words+" ")
			if i!=0 and (i+1)%4 == 0:
				template.write("\n\\newline\n")
			i+=1

		
		template.write("} \n")
		template.write("\\cvnumberphone{"+config["general"]["phone"]+"} % Phone number\n")
		template.write("\\cvmail{"+config["contact"]["mail"]+"} \n")
		template.write("\\cvsite{"+config["general"]["website"]+"}\n")

		template.write("\\begin{document}\n")
		template.write("\\aboutme{}\n")

		template.write("\\skills{\n")
		i=0
		for skill in config["skills"]["list"]:
			template.write("	{"+skill["skill"]+"/"+str(float(skill["rate"][:-1])*6/100)+"}")
			if i < len(config["skills"]["list"])-1:
				template.write(",\n")
			i+=1
		template.write("}\n")

		template.write("\\skillss{\n")
		i=0
		for skill in config["general"]["languages"]:
			template.write("	{"+skill["language"]+" "+skill["level"]+"/"+str(float(skill["rate"][:-1])*6/100)+"}")
			if i < len(config["skills"]["list"])-1:
				template.write(",\n")
			i+=1
		template.write("}\n")


		template.write("\\makeprofile \n")
		template.write("\\section{CURRICULUM VITAE} \n\n")
		
		for section in config["sections"]:
			template.write("\n\\section{"+section["caption"]+"}\n")
			template.write("\n")
			template.write("\\begin{twentyshort}\n")
			for item in section["list"]:
				template.write("\\twentyitemshort{\\footnotesize "+item["date"]+"}{["+item["title"]+"]"+item["label"]+"\n\\newline\n "+item["description"].replace("\n","\\\\")+" }\n")
				template.write("\\\\\n")
			template.write("\\end{twentyshort}\n\\\\")

		template.write("\\section{"+config["certification"]["caption"]+"}\n\n")

		template.write("\\begin{twenty}\n")

		for certification in config["certification"]["list"]:
			template.write("\\twentyitem{"+certification["date"]+"}{"+certification["institution"]+"}{}{"+certification["title"]+" "+certification["description"]+"}\n")

		template.write("\\end{twenty}\n")



		template.write("\\end{document}\n")
		template.close()

	os.system(". "+os.path.dirname(os.path.realpath(__file__))+"/compile.sh "+config["general"]["photo"]+" "+config["cv"]["link"])


if __name__ == '__main__':
	with open("../fr.json","r") as file_config:
		create_template(json.loads(file_config.read()))
		file_config.close()
