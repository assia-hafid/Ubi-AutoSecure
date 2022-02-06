from typing import TextIO

from core.database.jsonParsers import load, save
from core.database.processing import getAllHostsDifferences
from core.models.Host import Host
from core.models.Port import Port
from utils.constants import VALUES,DATABASE


def saveUpdatedHosts(diffHosts: list[Host], oldHosts: list[Host], jsonFile=DATABASE.JSON_PATH):

    if oldHosts is None:
        # This is the first scan, so saving it directly
        save(jsonFile, diffHosts)
    else:
        for diffHost in diffHosts:
            oldHostIndex = findHostIndex(oldHosts, diffHost)
            if oldHostIndex == -1:
                oldHosts.append(diffHost)
            else:
                # Check we're not in a case of a "Not Found" device
                if diffHost.state is not None:
                    updateHost(oldHosts, oldHostIndex, diffHost)
        save(jsonFile, oldHosts)


def updateHost(oldHosts: list[Host], oldHostIndex: int, diffHost: Host):
    if diffHost.addressType.find(VALUES.NOT_CHANGED) == -1:
        oldHosts[oldHostIndex].addressType = diffHost.addressType
    if diffHost.state.find(VALUES.NOT_CHANGED) == -1:
        oldHosts[oldHostIndex].state = diffHost.state

    for diffPort in diffHost.ports:
        oldPortIndex = findPortIndex(oldHosts[oldHostIndex].ports, diffPort)
        if oldPortIndex == -1:
            oldHosts[oldHostIndex].ports.append(diffPort)
        else:
            updatePort(oldHosts[oldHostIndex].ports, oldPortIndex, diffPort)


def updatePort(oldPorts: list[Port], oldPortIndex: int, diffPort: Port):
    if diffPort.protocol.find(VALUES.NOT_CHANGED) == -1:
        oldPorts[oldPortIndex].protocol = diffPort.protocol
    if diffPort.state.find(VALUES.NOT_CHANGED) == -1:
        oldPorts[oldPortIndex].state = diffPort.state
    if diffPort.service.find(VALUES.NOT_CHANGED) == -1:
        oldPorts[oldPortIndex].service = diffPort.service


def findHostIndex(hosts: list[Host], host: Host):
    for i in range(len(hosts)):
        if hosts[i].address == host.address:
            return i
    return -1


def findPortIndex(ports: list[Port], port: Port):
    for i in range(len(ports)):
        if ports[i].portId == port.portId:
            return i
    return -1
