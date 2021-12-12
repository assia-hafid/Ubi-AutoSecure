from core.Port import Port
from core.VulnsReport import VulnsReport
from typing import List

class Host:

    def __init__(self):
        self.address = ""
        self.addressType = ""
        self.state = ""
        self.ports = []
        self.vulnsReport = VulnsReport()


    # def __init__(self, address, addressType, state, ports):
    #     self.address = address
    #     self.addressType = addressType
    #     self.state = state
    #     self.ports = ports

