import os
from utils.bcolors import bcolors

def checkRootPerms():
    if(os.getuid() != 0):
        print(bcolors.FAIL+"You need root permissions to do run the script!")
        exit(1)
