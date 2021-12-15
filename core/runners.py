import subprocess

def runCommand(cmd):
    process = subprocess.Popen(cmd,stdout=subprocess.PIPE)
    code = process.wait()
    return code