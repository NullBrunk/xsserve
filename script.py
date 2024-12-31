import netifaces

def filter_function(value):
	return not value.startswith("br-") and not value.startswith("dock
er") and not value == "lo"

for inet in filter(filter_function, netifaces.interfaces()):
	iface = netifaces.ifaddresses("wlo1")[netifaces.AF_INET][0]["addr"]
