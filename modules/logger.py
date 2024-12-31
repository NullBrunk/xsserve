from termcolor import colored 
from time import strftime 

def abstract_log(text: str, color: str, log_text:str, important: bool = False, date_color: str = "light_blue"):
    attrs = []
    lb = colored("[", "white")
    rb = colored("]", "white")
    print(lb + colored(strftime("%H:%M:%S"), date_color) + rb, end=" ")
    print(lb, end="")
    if(important):
        attrs = ["bold"]
    print(colored(log_text, color, attrs=attrs) + colored("] ", "white") + colored(text, "white", attrs=attrs))


def info(text: str, important: bool = False):
    abstract_log(text=text, color="light_green", log_text="INFO", important=important)

def warning(text: str, important: bool = False):
    abstract_log(text=text, color="yellow", log_text="WARNING", important=important)

def error(text: str):
    abstract_log(text=text, color="red", log_text="ERROR", important=True)

def critical(text: str):
    abstract_log(text=text, color="red", log_text="CRITICAL", important=True)