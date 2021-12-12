"""
This is the main entry point of the script

usage: main.py -target <target> -interface [interface]

"""

import argparse
from collections import defaultdict
import IOTScanner
from scanners.nampScanners import scanHostPorts
from core.parsers import getHosts
from utils.printUtils import printHosts
from utils.printUtils import printLogo

# Parsing command line arguments
parser = argparse.ArgumentParser(description="Run IOTScanner")
parser.add_argument("-target",metavar="X/Y",required=True, help="Host or range to scan", )
parser.add_argument("-interface",metavar="ethX",required=False, help="Interface to use, optional", default="")
parser.add_argument("-scanType",metavar="Ex: -p-",required=False, help="Scan Type for nmap, -F, -p-, or define a range", default="-F")
parser.add_argument("-persist",required=False, help="persist nmap remort in /tmp")


args = parser.parse_args()

#Credits
printLogo()

# Start the app
IOTScanner.startScan(args.target, args.interface,args.scanType, args.persist)
