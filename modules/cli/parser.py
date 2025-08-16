from argparse import ArgumentParser
from random import randint

def parser():
	parser = ArgumentParser(description="Simplify XSS/CSRF exploitation")
	parser.add_argument("-p", "--port", help="The port to listen on (default: random(65000, 65100))", type=int, required=False)
	parser.add_argument("-n", "--ngrok", help="Auto-serve publicly with ngrok", required=False, action='store_true')
	parser.add_argument("-v", "--verbose", help="Show HTTP requests headers", required=False, action='store_true')

	args = parser.parse_args()

	if(args.port):
		port = args.port
	else:
		port = randint(65000, 65100)

	return port, args.ngrok, args.verbose