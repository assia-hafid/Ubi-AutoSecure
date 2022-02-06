from core.models.Port import Port
from core.models.VulnsReport import VulnsReport


class Host:

    def __init__(self):
        self.address = ""
        self.addressType = ""
        self.state = ""
        self.ports:list[Port] = []

        # This attribute is only used for XML Report generation
        self.vulnsReport = VulnsReport()
