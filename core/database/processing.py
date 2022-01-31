

from core.Host import Host
from core.Port import Port


def getAllHostsDifferences(actualHosts, oldHosts):
    diffs = []
    for actualHost in actualHosts:
        foundHost = findInHosts(oldHosts, actualHost.address)
        diffHost = getHostDifferences(actualHost, foundHost)
        if(isHostChanged(diffHost)):
            diffs.append(diffHost)
    
    diffs = completeWithOld(actualHosts, oldHosts)

    return diffs


def findInHosts(hosts, hostAddress):
    for host in hosts:
        if host.address == hostAddress:
            return host
    return None

def getHostDifferences(actualHost, oldHost):
    # This means a new device has been added
    if oldHost == None:
        return actualHost
    diff = Host()
    diff.address = None if actualHost.address == oldHost.address else actualHost.address
    diff.addressType = None if actualHost.addressType == oldHost.addressType else actualHost.addressType 
    diff.state = None if actualHost.state == oldHost.state else actualHost.state
    diffPorts = []
    for actualPort in actualHost.ports:
        foundPort = findInPorts(actualHost.ports,actualPort)
        diffPort = getPortsDifferences(actualPort,foundPort)
        diffPorts.append(diffPort)
    
    diff.ports = diffPorts
    return diff
    


def getPortsDifferences(actualPort, oldPort):
    # This means a new port has been added
    if oldPort == None:
        return actualPort
    diff = Port()
    diff.protocol = None if actualPort.protocol == oldPort.protocol else actualPort.protocol
    diff.portId = None if actualPort.portId == oldPort.portId else actualPort.portId
    diff.state = None if actualPort.state == oldPort.state else actualPort.state
    diff.state = None if actualPort.state == oldPort.state else actualPort.state
    return diff


def findInPorts(ports, portId):
    for port in ports:
        if port.portId == portId:
            return port
    return None

def isHostChanged(host):
    return host.address != None or host.addressType != None or host.state != None or isPortsChanged(host.ports)


def isPortsChanged(ports):
    for port in ports:
        if isPortChanged(port):
            return True
    return False

def isPortChanged(port):
    return port.protocol != None or port.portId != None or port.state != None or port.service != None