from core.Port import Port
from core.VulnsReport import VulnsReport
from typing import List

class Host:

    def __init__(self):
        self.address = ""
        self.addressType = ""
        self.state = ""
        self.ports = []

        # This attribute is only used for XML Report generation
        self.vulnsReport = VulnsReport()




