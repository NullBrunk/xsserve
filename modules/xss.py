from modules.logger import info, warning, error, critical 
from modules.httpserver import HttpServer
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

    def http_launcher(this, port):
        hs = HttpServer(port)
        try:
            hs.run()
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
            
            
        this.http_launcher(port)
