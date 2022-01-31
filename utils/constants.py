class DEFAULT_VALUES:
    DEFAULT_SCANPROTOCOL="TCP"
    DEFAULT_SCANTYPE="FAST"
    DEFAULT_DELETE_TEMP_FILE=False

class PREDEFINED_VALUES:
    SCANPROTOCOL = ["TCP","UDP"]
    SCANTYPES = ["FAST", "ALL"]
    BASIC_NSE_CATEGORIES = [
        "vuln",
        #"safe"
    ]
    
class DIRECTORIES:
    NSE_DIR = "resources/NSE/"

class LINKS:
    NSE_USAGE = "https://nmap.org/book/nse-usage.html"