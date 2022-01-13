import os
import amino
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
print("----------------------------")
value=int(input(f"""\33[93;5;5m\33[93;5;234m
1 - FOR GLOBAL PROFILE
2 - FOR COMMUNITY PROFILE

ENTER NUMBER: \33[0m\33[93;5;235m\33[93;5;5m \33[0m"""))

if value==1:
	exec(open('global.py').read())
elif value==2:
	exec(open('community.py').read())
	