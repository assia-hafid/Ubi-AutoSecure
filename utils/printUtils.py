from core.models.Host import Host
from core.database.processing import getGroupedHosts
from prettytable import PrettyTable
from utils.printColors import *
from utils.constants import VALUES


def printHosts(hosts: list[Host]):
    print("Printing parsed data...")
    index = 1
    for host in hosts:
        print("Host " + str(
            index) + ":   [ " + bcolors.BOLD + host.address + bcolors.ENDC + " ] | status: " + formatState(
            host.state) + " | type: " + host.addressType)
        table = PrettyTable()
        table.field_names = ["port", "protocol", "state", "service"]
        for port in host.ports:
            table.add_row([port.portId, port.protocol, formatState(port.state), port.service])

        print(table)
        index = index + 1


def formatState(state: str):
    if state == "open" or state == "up":
        return bcolors.BOLD + bcolors.OKGREEN + state + bcolors.ENDC
    return state


def printLogo():
    f = open("logo.txt")
    file_contents = f.read()
    print(file_contents)


def getLogo():
    f = open("logo.txt")
    file_contents = f.read()
    return file_contents


def printComparison(diffsHosts: list[Host]):
    groupedHosts = getGroupedHosts(diffsHosts)
    foundHosts = groupedHosts["found"]
    notFoundHosts = groupedHosts["notfound"]
    print("Found " + printGreenBold(str(len(foundHosts))) + " Host in this scan")
    index = 1
    for diffHost in foundHosts:
        print("Host " + str(index) + ":   [ " + printGreen(diffHost.address) + " ] | status: " +
              printChanged(diffHost.state) + " | type: " + printChanged(diffHost.addressType))
        table = PrettyTable()
        table.field_names = ["port", "protocol", "state", "service"]
        for port in diffHost.ports:
            table.add_row([port.portId, printChanged(port.protocol), printChanged(formatState(port.state)),
                           printChanged(port.service)])

        print(table)
        index += 1

    print("You have "+printBlueBold(str(len(notFoundHosts))) +
          " Host from your previous scans, but not detected in this one")
    index = 1
    for notFoundHost in notFoundHosts:
        print("Host " + str(index) + ":   [ " + printBlue(notFoundHost.address) +
              " ] | last know type: " + notFoundHost.addressType)
        index += 1


def printChanged(value: str):
    if value.find(VALUES.NOT_CHANGED) == -1:
        return printBold(value)
    return value
