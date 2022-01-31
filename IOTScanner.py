from scanners.nampScanners import scanHostsPorts
from core.parsers import getHosts
from utils.printUtils import printHosts
from utils.printUtils import printComparaison
from utils.generators import generateVulnsReport
from utils.constants import DEFAULT_VALUES
from core.database.Comparaison import getComparaisonReport

def startScan(targets, interface="",scanProtocol=DEFAULT_VALUES.DEFAULT_SCANPROTOCOL,scanType=DEFAULT_VALUES.DEFAULT_SCANTYPE,persist=DEFAULT_VALUES.DEFAULT_DELETE_TEMP_FILE):
    
    reportFile = scanHostsPorts(hosts=targets,interface=interface,scanProtocol=scanProtocol,scanType=scanType)
    
    hosts = getHosts(file=reportFile, persistTemp=persist)
    
    # Input in command line (hosts, ports and services)
    printHosts(hosts)

    #Input in XML file 
    generateVulnsReport(hosts)

    # Make comparaison with old data
    jsonFileTemp = "/home/assia/Documents/Ubi-AutoSecure/core/database/data/hostsTemp.json"
    diffs = getComparaisonReport(jsonFileTemp, hosts)
    printComparaison(diffs)


    # Store in database (JSON)


    #storeData(hots)
    #   1- load old data from JSON->Object to compare with actual data (Object)
    #   2- print comparaison results (what's added and what's removed) (we can even save a report of this comparaison)
    #   3- save the actual (new) data