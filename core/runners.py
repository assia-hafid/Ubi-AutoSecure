import subprocess

def runCommand(cmd):
    process = subprocess.Popen(cmd,stdout=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return {"stdout":stdout,"stderr":stderr}