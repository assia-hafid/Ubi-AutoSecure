from core.runners import runCommand
from utils.generators import getRandomString
from utils.bcolors import bcolors

def scanHostPorts(host, interface="",reportPath="", scanType="-F"):
    '''
    This function scan all ports in a given host, and store
    the results as an XML file in /tmp with a random name if 
    the "reportPath" variable not specified.
    This function returns the stdanrd output of the nmap scann command
    '''

    print(bcolors.OKGREEN+"Start scanning"+bcolors.ENDC)

    #Prepare file name if reportPath not specified
    print("Creating temporary report file...")
    newReportPath = ""
    if(reportPath == ""):
        filename = getRandomString(16)
        newReportPath = "/tmp/"+filename+".xml"
    else:
        newReportPath = reportPath


    # Running the scan based on the interface variable
    if(interface != ""):
        output = runCommand(["nmap","-sT",scanType,"--version-intensity","0","--script=vulners.nse","-A",host,"-e",interface, "-oX", newReportPath])
    else:
        output = runCommand(["nmap","-sT",scanType,"--version-intensity","0","--script=vulners.nse","-A",host,"-oX", newReportPath])

    #We may use the "output" later

    print(bcolors.OKGREEN+"Scan completed"+bcolors.ENDC)
    print("temporary report saved in: "+bcolors.BOLD+newReportPath+bcolors.OKBLUE+bcolors.ENDC)

    return newReportPath