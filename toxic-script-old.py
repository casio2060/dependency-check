import os, sys, json


print("\n> [INFO] - Test script for VSOSH_Project: list vulnerable (toxic) installed packages\n")

print("> [INFO] - Downloading list of Toxic Repos Started ...\n\n")

try:
	os.popen("wget https://raw.githubusercontent.com/toxic-repos/toxic-repos/main/data/json/toxic-repos.json").read()
	
	with open("toxic-repos.json", "r") as infile:
		toxic_bd = json.load(infile)

except Exception as e:
 	print("[ERROR] - No internet connection:\n", e)

try:
	os.popen("apt list --installed > installed-pkges-list.txt").read()
  
	list_of_pkgs = open("installed-pkges-list.txt", "r").read().split('\n')
	
	data = []
	for pkg in list_of_pkgs:
		pure_pkg_name = pkg[:pkg.find("/")]
		data.append(pure_pkg_name)
			
	print("> [INFO] - List of installed packages is saved to installed-pkges-list.txt\n\n")
	
	is_any_toxic_pkg_found = False
	for record in toxic_bd:
		for pkg_name in data[1:]:
			if len(pkg_name) and pkg_name.lower() == record.get('name').lower():
				is_any_toxic_pkg_found = True
				print(" [POSSIBLE TOXIC PACKAGE DETECTED]\n"
				f" > via match by package name: { pkg_name }\n",
				"[ADDITIONAL INFO PROVIDED]\n\n",
				f"id           : {record.get('id')}\n",
				f"name         : {record.get('name')}\n",
				f"problem type : {record.get('problem_type')}\n",
				f"description  : {record.get('description')}\n",
				f"commit link  : {record.get('commit_link')}\n\n")
				
	if not is_any_toxic_pkg_found:
		print(" [NO TOXIC PACKAGES DETECTED]\n\n")
		
	print("> [INFO] - Done\n")

except Exception as e:
 	print(" [ERROR] - Something went wrong:\n", e)
