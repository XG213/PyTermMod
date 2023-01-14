import subprocess, sys
 
while True:
    term=input("cmd: ")

    if term.__contains__("pip install"):
        modulename = term.replace("pip install ", "")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', modulename])