import xml.etree.ElementTree as ET
# from Models.Host import Host
from core.models.Host import Host
from core.models.Port import Port
from core.models.VulnsReport import VulnsReport
from utils.bcolors import bcolors
import os


def getHosts(file: str, persistTemp=False):
    report = ET.parse(file)
    # data = json.dump(report)
    hostsXML = report.findall("host")
    hosts = []
    for hostXML in hostsXML:
        host = mapXMLHost(hostXML)
        vulns = mapVulns(hostXML)
        host.vulnsReport = vulns
        hosts.append(host)

    if not persistTemp:
        # Deleting temporary file after parsing 
        print(bcolors.OKBLUE + "Deleting temporary file after parsing")
        print(bcolors.BOLD + "NOTICE: You can diseable this feature by passing '-persist' option" + bcolors.ENDC)
        ####### BE CAREFUL ! DON'T TOUCH THIS LINE, IT COULD HURT YOUR SYSTEM ######
        os.remove(file)

    return hosts


def mapXMLHost(hostXML: ET.Element):
    host = Host()
    addressXML = hostXML.find("address")
    if "addr" in addressXML.attrib:
        host.address = addressXML.attrib["addr"]

    if "addrtype" in addressXML.attrib:
        host.addressType = addressXML.attrib["addrtype"]

    statusXML = hostXML.find("status")
    if "state" in statusXML.attrib:
        host.state = statusXML.attrib["state"]

    if hostXML.find("ports") is not None:
        portsXML = hostXML.find("ports").findall("port")
        for portXML in portsXML:
            host.ports.append(mapXMLPort(portXML))

    return host


def mapXMLPort(portXML: ET.Element):
    port = Port()
    if portXML is not None and "protocol" in portXML.attrib:
        port.protocol = portXML.attrib["protocol"]

    if portXML is not None and "portid" in portXML.attrib:
        port.portId = portXML.attrib["portid"]

    stateXML = portXML.find("state")
    if stateXML is not None and "state" in stateXML.attrib:
        port.state = stateXML.attrib["state"]

    serviceXML = portXML.find("service")
    if serviceXML is not None and "name" in serviceXML.attrib:
        port.service = serviceXML.attrib["name"]

    return port


def mapVulns(hostXML: ET.Element):
    vulnsReport = VulnsReport()
    portsXML = hostXML.find("ports").findall("port")
    if portsXML is None:
        return None
    for portXML in portsXML:
        port = mapXMLPort(portXML)
        scriptsXML = portXML.findall("script")
        vulnsReport.vulns.append({"port": port, "scripts": scriptsXML})

    return vulnsReport
