"""
This is the main entry point of the script

usage: main.py -target <target> -interface [interface]

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

# Check for root previleges

checkRootPerms()

# Parsing command line arguments
parser = argparse.ArgumentParser(description="Run IOTScanner")
parser.add_argument("-targets",metavar="X/Y",required=True, help="Host or range to scan", nargs="*")
parser.add_argument("-interface",metavar="ethX",required=False, help="Interface to use, optional", default="")
parser.add_argument("-scanProtocol",metavar="Ex: TCP or UDP",required=False,
                    help="Scan Protocol for nmap, TCP: -sT, UDP: -sU", default=DEFAULT_VALUES.DEFAULT_SCANPROTOCOL)
parser.add_argument("-scanType",metavar="Ex: ALL or FAST",required=False, help="Scan Type for nmap, FAST: -F, ALL: -p-", default=DEFAULT_VALUES.DEFAULT_SCANTYPE)
parser.add_argument("-persist",required=False, help="persist nmap report in /tmp",
                    default=DEFAULT_VALUES.DEFAULT_DELETE_TEMP_FILE, action='store_true')


args = parser.parse_args()

#Credits
printLogo()

# Start the app
IOTScanner.startScan(args.targets,args.interface,args.scanProtocol,args.scanType,args.persist)
