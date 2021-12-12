from scanners.nampScanners import scanHostPorts
from core.parsers import getHosts
from utils.printUtils import printHosts
from utils.generators import generateVulnsReport

def startScan(target, interface="",scanType="-F-", persist=False):
    reportFile = scanHostPorts(host=target,interface=interface, scanType=scanType)
    hosts = getHosts(file=reportFile, removeTemp=persist==None)
    
    # Input in command line (hosts, ports and services)
    printHosts(hosts)

    #Input in XML file 
    generateVulnsReport(hosts)