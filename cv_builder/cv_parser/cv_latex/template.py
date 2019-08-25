import json

def create_template(config):
	with open("template_auto.tex","w") as template:
		template.write("\\documentclass[letterpaper]{twentysecondcv}\n")
		template.write("\\usepackage[utf8]{inputenc}\n")

		template.write("\\profilepic{about-img.jpg} % Profile picture\n")
		template.write("\\cvname{"+config["general"]["name"].upper()+"} % Your name\n")
		template.write("\\cvjobtitle{\hspace{1.2cm}"+config["general"]["title"]+"}  % Job title/career\n")
		template.write("\\cvdate{09 Novembre 1995 a Lyon} % Date of birth\n") #TODO
		template.write("\\cvaddress{2 Rue Saint Exupery\n")#TODO
		template.write("\\newline\n")
		template.write("92360 ,Meudon la forêt\n")
		template.write("\\newline\n")
		template.write("France} \n")
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

		#todo langages

		template.write("\\makeprofile \n")
		template.write("\\section{CURRICULUM VITAE} \n")
		


if __name__ == '__main__':
	with open("../fr.json","r") as file_config:
		create_template(json.loads(file_config.read()))
		file_config.close()
