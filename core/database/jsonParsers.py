import json
import os
from core.models.Host import Host
from core.models.Port import Port

from utils.constants import DATABASE

def load(file: str):

    if not os.path.exists(file):
        with open(file, "w"):
            return None

    with open(file, "r+") as read_or_write_file:
        jsonHosts = json.load(read_or_write_file)
    hosts = []
    for jsonHost in jsonHosts:
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


def stringifyHosts(hosts: list[Host]):
    stringHosts = []
    for host in hosts:
        stringHost = {
            "host": host.address,
            "type": host.addressType,
            "state": host.state,
            "ports": stringifyPorts(host.ports)
        }
        stringHosts.append(stringHost)
    return stringHosts


def stringifyPorts(ports: list[Port]):
    stringPorts = []
    for port in ports:
        stringPort = {
            "portId": port.portId,
            "protocol": port.protocol,
            "state": port.state,
            "service": port.service
        }
        stringPorts.append(stringPort)
    return stringPorts


def save(file: str, hosts: list[Host]):
    with open(file, "w") as write_file:
        json.dump(stringifyHosts(hosts), write_file, indent=4)
