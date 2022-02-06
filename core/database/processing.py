from core.models.Host import Host
from core.models.Port import Port
from utils.constants import VALUES


def getAllHostsDifferences(actualHosts: list[Host], oldHosts: list[Host]):
    if oldHosts is None:
        return actualHosts
    diffHosts: list[Host] = []
    for actualHost in actualHosts:
        foundHost = findInHosts(oldHosts, actualHost.address)
        diffHost = getHostDifferences(actualHost, foundHost)
        diffHosts.append(diffHost)

    # Complete with old
    for oldHost in oldHosts:
        foundOldHost = findInHosts(diffHosts, oldHost.address)
        if foundOldHost is None:
            # This is just say the host was not found in the actual scan
            temp = Host()
            temp.address = oldHost.address
            temp.addressType = oldHost.addressType
            temp.ports = oldHost.ports
            temp.state = None
            diffHosts.append(temp)

    return diffHosts


def findInHosts(hosts: list[Host], hostAddress: str):
    for host in hosts:
        if host.address == hostAddress:
            return host
    return None


def getHostDifferences(actualHost: Host, oldHost: Host):
    # This means a new device has been added
    if oldHost is None:
        return actualHost
    diffHost = Host()
    diffHost.address = actualHost.address
    diffHost.addressType = actualHost.addressType
    if actualHost.addressType == oldHost.addressType:
        diffHost.addressType += VALUES.NOT_CHANGED

    diffHost.state = actualHost.state
    if actualHost.state == oldHost.state:
        diffHost.state += VALUES.NOT_CHANGED

    diffPorts:list[Port] = []
    for actualPort in actualHost.ports:
        foundPort = findInPorts(oldHost.ports, actualPort.portId)
        diffPort = getPortsDifferences(actualPort, foundPort)
        diffPorts.append(diffPort)

    diffHost.ports = diffPorts

    return diffHost


def getPortsDifferences(actualPort: Port, oldPort: Port):
    # This means a new port has been added
    if oldPort is None:
        return actualPort
    diffPort = Port()
    diffPort.portId = actualPort.portId
    diffPort.protocol = actualPort.protocol
    if actualPort.protocol == oldPort.protocol:
        diffPort.protocol += VALUES.NOT_CHANGED

    diffPort.state = actualPort.state
    if actualPort.state == oldPort.state:
        diffPort.state += VALUES.NOT_CHANGED

    diffPort.service = actualPort.service
    if actualPort.service == oldPort.service:
        diffPort.service += VALUES.NOT_CHANGED

    return diffPort


def findInPorts(ports: list[Port], portId: str):
    for port in ports:
        if port.portId == portId:
            return port
    return None


def getGroupedHosts(hosts: list[Host]):
    """
    This function split hosts into "found" and "notfound hosts"
    based on the attribute "state"
    Returns a dictionary with two fields:
        - changed
        - unchanged
    """
    groupedHosts: dict[str, list[Host]] = {
        "found": [],
        "notfound": []
    }
    for host in hosts:
        if host.state is not None:
            groupedHosts["found"].append(host)
        else:
            groupedHosts["notfound"].append(host)
    return groupedHosts
