from core.runners import runCommand
from core.models.Host import Host
from utils.generators import getRandomString
from utils.bcolors import bcolors
from utils.constants import DIRECTORIES, PREDEFINED_VALUES, LINKS
import os


def scanHostsPorts(hosts: list[Host], interface="", reportPath="", scanProtocol="-sT", scanType="-F", vulns=False):
    """
    This function scan all ports in a given host, and store
    the results as an XML file in /tmp with a random name if
    the "reportPath" variable not specified.
    This function returns the standard output of the nmap scan command
    """

    print(bcolors.OKGREEN + "Start scanning" + bcolors.ENDC)

    # Prepare file name if reportPath not specified
    print("Creating temporary report file...")
    newReportPath = ""
    if reportPath == "":
        filename = getRandomString(16)
        newReportPath = "/tmp/" + filename + ".xml"
    else:
        newReportPath = reportPath

    # Running the scan based on the interface variable

    ## Constructing our NSE's scripts, the predefined in NMAP + User defined scripts in resources/NSE

    ### Check if the path exists : 
    NSECategories = ",".join(PREDEFINED_VALUES.BASIC_NSE_CATEGORIES)
    if vulns is True:
        if os.path.isdir(DIRECTORIES.NSE_DIR):
            NSECommand = "--script=" + NSECategories + "," + os.path.abspath(DIRECTORIES.NSE_DIR) + "/"
        else:
            print(bcolors.FAIL + "Custom NSE Resources not found, performing tests with basic categories: " + str(
                PREDEFINED_VALUES.BASIC_NSE_CATEGORIES) + bcolors.ENDC)
            NSECommand = "--script=" + NSECategories
            print("NSE Options: " + NSECommand)
            print("To learn more about NSE Categories: " + LINKS.NSE_USAGE)
    else:
        NSECommand = ""

    scanRangeNmap = getPortRangeScanType(scanType)
    scanProtocolType = getProtocolScanType(scanProtocol)
    # We use the spread operator '*' to concatenate the "baseCommande" list with the interface options
    baseCommande = ["nmap", "-T5", scanProtocolType, scanRangeNmap, *hosts, "-oX", newReportPath]
    if (interface != ""):
        cmd = [*baseCommande, "-e", interface]

    else:
        cmd = baseCommande

    if NSECommand != "":
        cmd = [*baseCommande, NSECommand]

    # Just converting the list to a string, joining elements with a " " space. to get the executed command
    print(bcolors.OKCYAN + "executing command: " + " ".join(cmd) + bcolors.ENDC)

    # Timeout should be passed as arg in CLI if needed
    exitCode = runCommand(cmd)

    if exitCode != 0:
       print(bcolors.FAIL + "Nmap command exited with error code: " + str(exitCode) + bcolors.ENDC)
       exit(1)


    print(bcolors.OKGREEN + "Scan completed" + bcolors.ENDC)
    print("temporary report saved in: " + bcolors.BOLD + newReportPath + bcolors.OKBLUE + bcolors.ENDC)

    return newReportPath


def getPortRangeScanType(scanType: str):
    if scanType == "FAST":
        return "-F"
    if scanType == "ALL":
        return "-p-"


def getProtocolScanType(scanProtocol: str):
    if scanProtocol == "TCP":
        return "-sT"
    if scanProtocol == "UDP":
        return "-sU"
