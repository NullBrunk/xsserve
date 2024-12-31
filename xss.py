#!/usr/bin/env python3

from modules.logger import info, error 
from modules.ngrok import killer
from termcolor import colored
from modules.xss import XSS
from random import randint

def banner():
    """
    Display the script banner
    """
    print(
        colored(f"""\n __  _____ ___  ___ _ ____   _____ \n""", "yellow", attrs=["bold"]) +
        colored(f""" \\ \\/ / __/ __|/ _ \\ '__\\ \\ / / _ \\\n""", "yellow", attrs=["bold"]) +
        colored(f"""  >  <\\__ \\__ \\  __/ |   \\ V /  __/""", "yellow", attrs=["bold"]) + colored("    Simplify XSS exploitation\n", "white") +
        colored(f""" /_/\\_\\___/___/\\___|_|    \\_/ \\___|""", "yellow", attrs=["bold"]) + colored("    (", "white") + colored("@NullBrunk", "red") + colored(")\n", "white")
    ) 

if __name__ == "__main__":
    banner()
    info("launching XSS.py")
    
    xss = XSS()
    try:
        xss.run(randint(65000, 65500))
    except KeyboardInterrupt:
        print()
        error("user exit")
    killer()