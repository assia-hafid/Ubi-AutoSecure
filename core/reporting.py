from pathlib import Path
from xml.dom import minidom
from core.models.Host import Host
from utils.bcolors import bcolors
import xml.etree.ElementTree as ET
from utils.generators import getFileNameDateTime


def generateVulnsReport(hosts: list[Host]):
    print("Start generating vulnerabilities report...")

    # Creating reports folder if not exist
    Path("reports").mkdir(parents=True, exist_ok=True)

    # generate the filename based on the datetime
    filename = getFileNameDateTime("vulns-report") + ".xml"

    XMLReport = ET.Element("report")
    for host in hosts:
        XMLHost = ET.SubElement(XMLReport, "host")
        XMLAddress = ET.SubElement(XMLHost, "address")
        XMLAddress.text = host.address
        countVulns = 0
        for vuln in host.vulnsReport.vulns:
            if (vuln["scripts"] != None):
                XMLVulns = ET.SubElement(XMLHost, "vulnerabilities")
                XMLPort = ET.SubElement(XMLVulns, "port")
                XMLPort.text = vuln["port"].portId
                XMLOutput = ET.SubElement(XMLVulns, "output")
                scriptsCount = 1
                for script in vuln["scripts"]:
                    XMLScripts = ET.SubElement(XMLOutput, "scripts")
                    XMLScripts.insert(scriptsCount, script)
                    scriptsCount = scriptsCount + 1
                    countVulns = countVulns + 1

        if countVulns == 0:
            print(bcolors.WARNING + "No vulnerabilities found for" + host.address + bcolors.ENDC)
        else:
            print(bcolors.OKCYAN + "Found [" + str(
                countVulns) + "] possible vulnerability for " + host.address + bcolors.ENDC)

    with open("reports/" + filename, 'w+') as f:
        xmlstr = minidom.parseString(ET.tostring(XMLReport)).toprettyxml(indent="   ")
        f.write(xmlstr)

    print(
        bcolors.OKGREEN + "vulnerabilities report generated sucessfully at: [ " + bcolors.BOLD + "reports/" + filename + " ]" + bcolors.ENDC)
