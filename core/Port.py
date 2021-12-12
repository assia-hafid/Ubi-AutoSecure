class Port:

    def __init__(self):
        self.protocol = ""
        self.portId = ""
        self.state = ""
        self.service = ""
        self.vulns = []

    # def __init__(self, protocol, portId, state, service):
    #     self.protocol = protocol
    #     self.portId = portId
    #     self.state = state
    #     self.service = service