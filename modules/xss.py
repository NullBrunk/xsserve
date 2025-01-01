from modules.logger import info, warning, error, critical
from netifaces import interfaces, AF_INET, ifaddresses
from modules.httpserver import HttpServer
from modules.ngrok import ngrok, killer


class XSS:
    def __init__(this):
        pass

    def filter_interfaces(this, value):
        return not value.startswith("br-") and not value.startswith("docker") and not value == "lo"

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


        for inet in filter(this.filter_interfaces, interfaces()):
            iface_ip = ifaddresses(inet)[AF_INET][0]["addr"]
            info(f"listening on http://{iface_ip}:{port}/", True)

        this.http_launcher(port)
