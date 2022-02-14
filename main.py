"""
This is the main entry point of the script

usage: python3 main.py -targets X.X.X.X [-scanType {ALL|FAST}] [-scanProtocol {TCP|UDP}] [-interface "name"] [-persist] [-vulns] 

"""

import argparse
from collections import defaultdict
import IOTScanner
from scanners.nampScanners import scanHostsPorts
from core.parsers import getHosts
from utils.printUtils import printHosts
from utils.printUtils import printLogo
from utils.constants import DEFAULT_VALUES
from utils.checkers import checkRootPerms



# Parsing command line arguments
parser = argparse.ArgumentParser(description="Run IOTScanner")
parser.add_argument("-targets",metavar="X/Y",required=True, help="Host or range to scan", nargs="*")
parser.add_argument("-interface",metavar="ethX",required=False, help="Interface to use, optional", default="")
parser.add_argument("-scanProtocol",metavar="Ex: TCP or UDP",required=False,
                    help="Scan Protocol for nmap, TCP: -sT, UDP: -sU", default=DEFAULT_VALUES.DEFAULT_SCANPROTOCOL)
parser.add_argument("-scanType",metavar="Ex: ALL or FAST",required=False, help="Scan Type for nmap, FAST: -F, ALL: -p-", default=DEFAULT_VALUES.DEFAULT_SCANTYPE)
parser.add_argument("-persist",required=False, help="persist nmap report in /tmp",
                    default=DEFAULT_VALUES.DEFAULT_DELETE_TEMP_FILE, action='store_true')
parser.add_argument("-vulns", required=False,help="enable vulnerabilities scan for performance", action='store_true', default=False)


args = parser.parse_args()

# Check for root previleges

checkRootPerms(args.scanProtocol)

#Credits
printLogo()

# Start the app
IOTScanner.startScan(args.targets,args.interface,args.scanProtocol,
                    args.scanType,args.persist, args.vulns)
