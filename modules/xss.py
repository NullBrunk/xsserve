from modules.logger import info, warning, error, critical 
from modules.webserver import WebServer
from modules.ngrok import ngrok, killer
import netifaces

class XSS:
    def __init__(this) -> None:
        pass

    def ngrok_launcher(this, port):
        this.pub_ip = ngrok(port)

        if(this.pub_ip == False):
            critical("could not launch ngrok")
            warning("Killing ngrok")
            killer()
            exit()

        this.pub_ip = "http" + this.pub_ip[3:] + "/"

    def webserver_launcher(this, port):
        ws = WebServer(port)
        try:
            ws.run()
        except Exception as e:
            critical("server error")
            print(e)
            killer()

    def run(this, port):
        try:
            pass
            this.ngrok_launcher(port)
        except KeyboardInterrupt:
            error("user exit")
            killer()
        except:
            killer()
        info(f"listening on {this.pub_ip}", True)
        info(f"listening on http://0.0.0.0:{port}/", True)
            
            
        this.webserver_launcher(port)
