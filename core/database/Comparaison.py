from core.database.jsonParsers import load
from core.database.processing import getAllHostsDifferences

def getComparaisonReport(jsonFile,actualHosts):
    oldHosts = load(jsonFile)
    return getAllHostsDifferences(actualHosts, oldHosts)


def saveUpdatedHosts(diffHosts, jsonFile):
    oldHosts = load(jsonFile)
    for diffHost in diffHosts:
        oldHosts = updateHost(oldHosts, diffHost)
    

def updateHost(oldHosts, diffHost):
    for i in range(len(oldHosts)):
        if oldHosts[i].address == diffHost.address:
            if diffHost.type != None:
                oldHosts[i].type = diffHost.type
            if diffHost.state != None:
                oldHosts[i].state = diffHost.state

            # TODO: Iterate on ports of a host, and update them !!!
            
            

def updatePort(oldPorts, diffPort):
    for i in range(len(oldPorts)):
        if oldPorts[i].portId == diffPort.portId:
            if diffPort.protocol != None:
                oldPorts[i].protocol = diffPort.protocol
            if diffPort.state != None:
                oldPorts[i].state = diffPort.state
            if diffPort.service != None:
                oldPorts[i].service = diffPort.service