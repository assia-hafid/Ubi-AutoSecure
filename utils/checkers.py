import os
from utils.bcolors import bcolors
from core.models.Host import Host
from core.models.Port import Port
from utils.constants import VALUES


def checkRootPerms(scanProtocol: str):
    if scanProtocol == "UDP" and os.getuid() != 0:
        print(bcolors.FAIL + "You need root permissions to do run the script!")
        exit(1)


def isHostChanged(host: Host):
    return host.address.find(VALUES.NOT_CHANGED) != -1 \
           or host.addressType.find(VALUES.NOT_CHANGED) != -1 \
           or host.state.find(VALUES.NOT_CHANGED) != -1 \
           or isPortsChanged(host.ports)


def isPortsChanged(ports: list[Port]):
    for port in ports:
        if isPortChanged(port):
            return True
    return False


def isPortChanged(port: Port):
    return port.protocol.find(VALUES.NOT_CHANGED) != -1 \
           or port.portId.find(VALUES.NOT_CHANGED) != -1 \
           or port.state.find(VALUES.NOT_CHANGED) != -1 \
           or port.service.find(VALUES.NOT_CHANGED) != -1
