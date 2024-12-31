from requests import get
from time import sleep
from os import popen

def ngrok(port):
    ngrok_path = popen("whereis ngrok").read().strip()

    if(ngrok_path == "ngrok:"):
        return False

    popen(f"ngrok tcp {port}")
    sleep(2)
    # <PublicURL>tcp://6.tcp.eu.ngrok.io:10118</PublicURL>
    try:
        r = get("http://localhost:4040/api/tunnels")
    except:
        return False

    pub_ip = ""
    try:
        pub_ip = r.json()["tunnels"][0]["public_url"]
    except:
        try:
            sleep(2)
            pub_ip = r.json()["tunnels"][0]["public_url"]
        except:
            return False

    return pub_ip


def killer():
    popen("killall ngrok")
    exit()
