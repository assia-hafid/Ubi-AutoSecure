from utils.bcolors import bcolors


def printRed(data: str):
    return bcolors.FAIL + data + bcolors.ENDC


def printRedBold(data: str):
    return bcolors.FAIL + bcolors.BOLD + data + bcolors.ENDC


def printGreen(data: str):
    return bcolors.OKGREEN + data + bcolors.ENDC


def printGreenBold(data: str):
    return bcolors.OKGREEN + bcolors.BOLD + data + bcolors.ENDC


def printBold(data: str):
    return bcolors.BOLD + data + bcolors.ENDC


def printBlue(data: str):
    return bcolors.OKBLUE + bcolors.BOLD + data + bcolors.ENDC


def printBlueBold(data: str):
    return bcolors.OKBLUE + bcolors.BOLD + bcolors.BOLD + data + bcolors.ENDC