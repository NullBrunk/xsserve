from modules.cli.logger import info, warning, error, critical, colored
from netifaces import interfaces, ifaddresses, AF_INET
from modules.httpserver import HttpServer
from modules.ngrok import ngrok, killer

class XSS:
    def __init__(this, port, launch_ngrok, verbose):
        this.port = port
        this.pub_ip = False
        this.launch_ngrok = launch_ngrok
        this.verbose = verbose


    def ngrok_launcher(this):
        this.pub_ip = ngrok(this.port)

        if(this.pub_ip == False):
            critical("could not launch ngrok")
            warning("Killing ngrok")
            killer()
            exit()

        this.pub_ip = "http" + this.pub_ip[3:] + "/"


    def http_launcher(this, port):
        hs = HttpServer(port, this.verbose)
        try:
            hs.run()
        except Exception as e:
            critical("server error")
            print(e)
            killer()


    def show_ips(this):
        # Put the interfaces that you don't wanna show here
        # personnaly i always remove docker0. 
        skip = ["docker0"]

        # Uncomment this line if you don't want to skip any interface
        # skip = []
        
        # slice to remove loopback from the interfaces
        for inet in interfaces()[1:]:
            
            if(inet in skip):
                continue

            ip_addr = ifaddresses(inet)[AF_INET][0]["addr"]

            ip_and_port = f"{ip_addr}"
            if(this.port != 80):
                ip_and_port += f":{this.port}"


            info(f"listening on {colored(f'http://{ip_and_port}/', 'yellow')} ")

    def run(this):

        if(this.launch_ngrok):
            try:
                info("launching ngrok")
                this.ngrok_launcher()
            except KeyboardInterrupt:
                error("user exit")
                killer()
        print()


        this.show_ips()
        if(this.pub_ip):
            info(f"listening on {colored(f'{this.pub_ip}', 'yellow')} ")

        print()
        this.http_launcher(this.port)
