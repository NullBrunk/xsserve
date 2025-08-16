from modules.cli.logger import info, warning, colored
from mimetypes import guess_type
from os.path import abspath
from os import listdir
from re import search
import socket

class HttpServer:
    def __init__(this, port, verbose):
        this.HOST = '0.0.0.0'
        this.PORT = port
        this.files_path = ""
        this.verbose = verbose

    def extract(this, request):
        # Extract the answered path
        try:
            first_line = request.split('\r\n')[0]
            method, path, _ = first_line.split(' ')
        except ValueError:
            method, path = None, None

        return first_line, method, path

    def is_shared_file(this, path):
        this.files_path = "/".join(abspath(__file__).split("/")[:-1]) + "/../files"
        shared_files = listdir(this.files_path)

        if(path.startswith("/")):
            return path[1:] in shared_files

        return path in shared_files


    def run(this):
        this.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        this.server_socket.bind((this.HOST, this.PORT))
        this.server_socket.listen(5)


        while True:
            client_socket, client_address = this.server_socket.accept()

            # Get the client request
            request = client_socket.recv(1024)
            try:
                request = request.decode('utf-8')
            except:
                response = b"HTTP/1.1 500 Internal Server Error\r\n\r\n"
                client_socket.sendall(response)
                continue


            first_line, method, path = this.extract(request)
            response = b""

            if method == "GET" and this.is_shared_file(path):
                with open(this.files_path + path, "r") as file:
                    content = file.read()
                    response = (
                        "HTTP/1.1 200 OK\r\n"
                        f"Content-Type: {guess_type(path)[0]}\r\n"
                        "Content-Length: " + str(len(content)) + "\r\n\r\n" 
                        + content
                    ).encode('utf-8')
                info("served file " + colored(path, "red"), True)

            elif method == "GET" and path.startswith("/favicon.ico"):
                response = b"HTTP/1.1 404 Not Found\r\n\r\n"
                sc = None

            elif method== "POST":
                info("Received: " + colored(first_line, "red"))
                
                body = "\r\n\r\n".join(request.split("\r\n\r\n")[1:])
                if body.strip() == "":
                    body = "empty body"

                info(f"Body: " + colored(body, "red"), True)
                sc = 200
                
            else:
                info("Received: " + colored(first_line, "red"), True)
                sc = 404

            if(this.verbose):
                to_show = request.strip("\r\n").strip("\r\n").replace(first_line, "")
                print(to_show)

            client_socket.sendall(response)
            client_socket.close()

            if(sc == 200):
                info("sending a 200 OK reponse")
                response = b"HTTP/1.1 200 OK\r\n\r\n"
            elif(sc == 404):
                warning("sending a 404 Not Found reponse")
                response = b"HTTP/1.1 404 Not Found\r\n\r\n"

            print()
