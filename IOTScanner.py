from scanners.nampScanners import scanHostsPorts
from core.parsers import getHosts
from core.reporting import generateVulnsReport
from core.database.resultsDAO import saveUpdatedHosts
from core.database.jsonParsers import load
from core.database.processing import getAllHostsDifferences
from utils.printUtils import printComparison
from utils.constants import DEFAULT_VALUES,DATABASE


def startScan(targets, interface="",scanProtocol=DEFAULT_VALUES.DEFAULT_SCANPROTOCOL,
              scanType=DEFAULT_VALUES.DEFAULT_SCANTYPE,persist=DEFAULT_VALUES.DEFAULT_DELETE_TEMP_FILE, vulns=False):

    reportFile = scanHostsPorts(hosts=targets,interface=interface,scanProtocol=scanProtocol,scanType=scanType, vulns=vulns)
    
    hosts = getHosts(file=reportFile, persistTemp=persist, vulns=vulns)
    
    # Input in command line (hosts, ports and services)
    # printHosts(hosts)

    # Input in XML file
    if vulns is True:
        generateVulnsReport(hosts)
    
    # Load old hosts from json
    oldHosts = load(DATABASE.JSON_PATH)

    # Make comparison with old data
    diffs = getAllHostsDifferences(hosts,oldHosts)

    # Save new results
    saveUpdatedHosts(diffs, oldHosts)

    # Print new results
    printComparison(diffs)

