
from core.parsers import getHosts
from core.reporting import generateVulnsReport

hosts = getHosts("/tmp/y0ct1t6ic1M4Qw9E.xml")
generateVulnsReport(hosts)


