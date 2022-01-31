import json

from core.Host import Host
from core.Port import Port

def load(file):
    with open(file, "r") as read_file:
        jsonHosts = json.load(read_file)
    
    hosts = []
    for jsonHost in jsonHosts:
        #print(jsonHost["host"])
        host = Host()
        host.address = jsonHost["host"]
        host.addressType = jsonHost["type"]
        host.state = jsonHost["state"]
        for jsonPort in jsonHost["ports"]:
            port = Port()
            port.portId = jsonPort["portId"]
            port.protocol = jsonPort["protocol"]
            port.state = jsonPort["state"]
            port.service = jsonPort["service"]
            host.ports.append(port)
        
        hosts.append(host)
    
    return hosts
    
#load("/home/assia/Documents/Ubi-AutoSecure/core/database/data/hosts.json")