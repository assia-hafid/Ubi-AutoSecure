from scanners.nampScanners import scanHostsPorts
from core.parsers import getHosts
from utils.printUtils import printHosts
from utils.generators import generateVulnsReport
from utils.constants import DEFAULT_VALUES

def startScan(targets, interface="",scanProtocol=DEFAULT_VALUES.DEFAULT_SCANPROTOCOL,scanType=DEFAULT_VALUES.DEFAULT_SCANTYPE,persist=DEFAULT_VALUES.DEFAULT_DELETE_TEMP_FILE):
    
    reportFile = scanHostsPorts(hosts=targets,interface=interface,scanProtocol=scanProtocol,scanType=scanType)
    
    hosts = getHosts(file=reportFile, persistTemp=persist)
    
    # Input in command line (hosts, ports and services)
    printHosts(hosts)

    #Input in XML file 
    generateVulnsReport(hosts)