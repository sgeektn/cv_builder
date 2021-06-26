import json
import os
import subprocess

def create_template(config):
	
	with open(os.path.dirname(os.path.realpath(__file__))+"/page1sidebar.tex","w") as template:
		template.write("\\cvsection{"+config["skills"]["caption"]+"}\n")
		for skill in config["skills"]["list"]:
			template.write("\\cvskill{%s}{%s}\n"%(skill["skill"],str(int(float(skill["rate"][:-1])*5/100))))

		template.write("\\cvsection{"+config["certification"]["caption"]+"}\n")
		template.write("\\begin{itemize}\n")
		for certif in config["certification"]["list"]:
			template.write("\\item %s %s ( %s )\n"%(certif["title"],certif["description"],certif["institution"]))
		template.write("\\end{itemize}\n")

		template.write("\\cvsection{"+config["general"]["language_caption"]+"}\n")
		for language in config["general"]["languages"]:
			template.write("\\cvskill{%s}{%s}\n"%(language["language"]+" "+language["level"],str(int(float(language["rate"][:-1])*5/100))))

		template.close()

	with open(os.path.dirname(os.path.realpath(__file__))+"/template_auto.tex","w") as template:

		template.write("\\documentclass[10pt,a4paper]{altacv}\n")
		template.write("\\geometry{left=1cm,right=9cm,marginparwidth=6.8cm,marginparsep=1.2cm,top=1cm,bottom=1cm}\n")
		template.write("\\usepackage[utf8]{inputenc}\n")
		template.write("\\usepackage[T1]{fontenc}\n")
		template.write("\\usepackage[default]{lato}\n")
		template.write("\n")
		template.write("\\definecolor{VividPurple}{HTML}{2E64FE}\n")
		template.write("\\definecolor{SlateGrey}{HTML}{2E2E2E}\n")
		template.write("\\definecolor{LightGrey}{HTML}{666666}\n")
		template.write("\\colorlet{heading}{VividPurple}\n")
		template.write("\\colorlet{accent}{VividPurple}\n")
		template.write("\\colorlet{emphasis}{SlateGrey}\n")
		template.write("\\colorlet{body}{LightGrey}\n")
		template.write("\n")
		template.write("\\renewcommand{\\itemmarker}{{\\small\\textbullet}}\n")
		template.write("\\renewcommand{\\ratingmarker}{\\faCircle}\n")
		template.write("\n")
		template.write("\\DeclareUnicodeCharacter{0301}{}\n")
		template.write("\\DeclareUnicodeCharacter{0302}{}\n")
		template.write("\\begin{document}\n")	
		template.write("\\name{%s}\n"%(config["general"]["name"],))	
		template.write("\\tagline{%s}\n"%(config["general"]["title"],))	
		template.write("\\photo{3cm}{image}\n")
		template.write("\\personalinfo{\n")
		template.write("	\\email{%s}\n"%(config["contact"]["mail"],))
		template.write("	\\homepage{%s}\n"%(config["general"]["website"],))
		template.write("	\\phone{%s}\n"%(config["general"]["phone"],))
		template.write("	\\location{%s}\n"%(config["contact"]["adress"],))
		template.write("	\\dob{%s %s}\n"%(config["general"]["date_of_birth"],config["general"]["place_of_birth"]))
		template.write("}\n")
		template.write("\\begin{adjustwidth}{}{-8cm}\n")
		template.write("\\makecvheader\n")
		template.write("\\end{adjustwidth}\n")
		##todo make it fit with new pages
		template.write("\\marginpar{\\vspace*{\\dimexpr1pt-\\baselineskip}\\raggedright\\include{page1sidebar}}\n")

		for section in config["sections"]:
			template.write("\\cvsection{%s}\n"%(section["caption"],))
			for section_item in section["list"]:
				template.write("\\cvevent{}{%s | %s }{%s} {}\n"%(section_item["title"],section_item["label"],section_item["date"]))
				template.write("\\begin{itemize}\n")
				template.write("	\\item "+section_item["description"].replace("\n","\\\\")+" \n")
				template.write("\\end{itemize}\n")	
		template.write("\\end{document}\n")			
		template.close()

	with open("debug.txt","w") as debug:
		debug.write("Photo in json\n")
		debug.write(config["general"]["photo"]+"\n")
		debug.write(". "+os.path.dirname(os.path.realpath(__file__))+"/compile.sh "+config["general"]["photo"]+" "+config["cv"]["link"])
		debug.close()
	#os.system(". "+os.path.dirname(os.path.realpath(__file__))+"/compile.sh "+config["general"]["photo"]+" "+config["cv"]["link"])
	subprocess.call([os.path.dirname(os.path.realpath(__file__))+"/compile.sh",config["general"]["photo"],config["cv"]["link"]])
if __name__ == '__main__':
	with open("../fr.json","r") as file_config:
		create_template(json.loads(file_config.read()))
		file_config.close()

	
