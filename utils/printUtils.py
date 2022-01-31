from core.Host import Host
from typing import List
from utils.bcolors import bcolors
from prettytable import PrettyTable

def printHosts(hosts:List[Host]):
    print("Printing parsed data...")
    index = 1
    for host in hosts:
        print("Host "+str(index)+":   [ "+bcolors.BOLD+host.address+bcolors.ENDC+" ] | status: "+formatState(host.state)+" | type: "+host.addressType)
        table = PrettyTable()
        table.field_names = ["port", "protocol", "state","service"]
        for port in host.ports:
            table.add_row([port.portId,port.protocol,formatState(port.state),port.service])
        
        print(table)
        index = index + 1
        


def formatState(state):
    if state == "open" or state == "up":
        return bcolors.BOLD+bcolors.OKGREEN+state+bcolors.ENDC
    return state


def printLogo():
    f = open("logo.txt")
    file_contents = f.read()
    print(file_contents)

def getLogo():
    f = open("logo.txt")
    file_contents = f.read()
    return file_contents


def printComparaison(diffsHosts):
    print("Here is all the new things")
    index = 1
    for diffHost in diffsHosts:
        print("Host "+str(index)+":   [ "+bcolors.BOLD+printChanged(diffHost.address)+bcolors.ENDC+" ] | status: "+printChanged(diffHost.state)+" | type: "+printChanged(diffHost.addressType))
        table = PrettyTable()
        table.field_names = ["port", "protocol", "state","service"]
        for port in diffHost.ports:
            table.add_row([port.portId,printChanged(port.protocol),printChanged(formatState(port.state)),printChanged(port.service)])
        
        print(table)
        index = index + 1

def printChanged(value):
    if value == None:
        return "NOT CHANGED"
    return value
