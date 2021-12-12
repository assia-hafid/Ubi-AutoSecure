import random, string
from pathlib import Path
from datetime import datetime
import xml.etree.ElementTree as ET
from utils.bcolors import bcolors
from xml.dom import minidom



def getRandomString(length):

    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length))
    return x

def generateVulnsReport(hosts):

    print("Start generating vulnerabilities report...")

    # Creating reports folder if not exist
    Path("reports").mkdir(parents=True, exist_ok=True)

    # generate the filename based on the datetime
    filename = getFileNameDateTime("vulns-report")+".xml"

    XMLReport = ET.Element("report")
    for host in hosts:
        XMLHost = ET.SubElement(XMLReport,"host")
        XMLAddress = ET.SubElement(XMLHost,"address")
        XMLAddress.text = host.address
        for tag in host.vulnsReport.scriptsTags:
            if(tag["script"] != None):
                XMLVulns = ET.SubElement(XMLHost,"vulnerabilities")
                XMLPort = ET.SubElement(XMLVulns,"port")
                XMLPort.text = tag["port"].portId
                XMLOutput = ET.SubElement(XMLVulns,"output")
                XMLOutput.insert(1,tag["script"])

    with open("reports/"+filename, 'w') as f:
        tree = ET.ElementTree(XMLReport)
        xmlstr = minidom.parseString(ET.tostring(XMLReport)).toprettyxml(indent="   ")
        f.write(xmlstr)

    print(bcolors.OKGREEN+"vulnerabilities report generated sucessfully at: [ "+bcolors.BOLD+"reports/"+filename+" ]"+bcolors.ENDC)
       
    

def getFileNameDateTime(prefix):
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
    return prefix+"-"+dt_string