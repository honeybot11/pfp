import os
os.system("pip install Dick.py==1.3.1")
os.system("clear")
import amino
import urllib
import names
from os import path
import random
import platform,socket,re,uuid
import json
import requests
from time import sleep
from fancy_text import fancy
from threading import Thread
from concurrent.futures import ProcessPoolExecutor
import requests
try:
    import colorama
except ModuleNotFoundError:
    os.system("pip install colorama")
    import colorama
try:
    import pyfiglet
except ModuleNotFoundError:
    os.system("pip install pyfiglet")
    import pyfiglet
from colorama import init, Fore, Back, Style
print("\n\33[93;5;5m\33[93;5;234m ❮ NAME AND PFP CHANGER : Made By Levi ❯ \33[0m\33[93;5;235m\33[93;5;5m \33[0m")
init()
print(Fore.GREEN + Style.BRIGHT)
print(pyfiglet.figlet_format("TECH", font="cybermedium"))
print(pyfiglet.figlet_format("VISION", font="cybermedium"))
THIS_FOLDER = path.dirname(path.abspath(__file__))
emailfile=path.join(THIS_FOLDER,"accounts.json")
dictlist=[]
with open(emailfile) as f:
    dictlist = json.load(f)
def log(cli : amino.Client,email : str, password : str):
    try:
        cli.login(email=email,password=password)
    except Exception as e:
    	print(e)
    	pass
def fancy_name():
	nm=''
	for i in names.get_first_name():
		nm=nm+i
	return nm
def geticon(client):
	urlx=client.get_all_users(size=100).profile.icon
	for url in urlx:
		if url is None or url=="None":
			pass
		else:
		  return url
		  break
def threadit(acc : dict):
    email=acc["email"]
    password=acc["password"]
    device=acc["device"]
    client=amino.Client(device)
    os.remove("device.json")
    log(cli=client,email=email,password=password)
    print("•·•·•·•·•·•·•·•·•·••·•·•·•·•·•·•·•")
    print(f"\33[93;5;5m\33[93;5;234m ❮ Logged In {email} ❯\33[0m\33[93;5;235m\33[93;5;5m \33[0m")
    try:
    	nick=fancy_name()
    	search="anime"
    	response = requests.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=W05ZAoiUU7fHjXgOXU1Rs6No2CSULZUc')
    	data = json.loads(response.text)
    	gif_choice = random.randint(0, 100)
    	image = data['data'][gif_choice]['images']['original']['url']
    	if image is not None:
    		filename="anime.png"
    		urllib.request.urlretrieve(image, filename)
    	img=open("anime.png","rb")
    	client.edit_profile(icon=img,nickname=nick)
    	print("\33[93;5;5m\33[93;5;234m ❮ Name changed ❯\33[0m\33[93;5;235m\33[93;5;5m \33[0m"+ nick)
    	print("\33[93;5;5m\33[93;5;234m ❮ ProfilePic changed ❯\33[0m\33[93;5;235m\33[93;5;5m \33[0m")
    except:
    	pass
    
    
  
def main():
    print(f"\33[93;5;5m\33[93;5;234m ❮ {len(dictlist)} ACCOUNTS LOADED ❯ \33[0m\33[93;5;235m\33[93;5;5m \33[0m")
    for amp in dictlist:
        threadit(amp)
    print(f"\n\n\33[93;5;5m\33[93;5;234m ❮ Pfp and Name changed for {len(dictlist)} ACCOUNTS ❯ \33[0m\33[93;5;235m\33[93;5;5m \33[0m")
    	         
if __name__ == '__main__':
	main()