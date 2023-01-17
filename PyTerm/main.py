#PyTerm, a simple terminal write with python

#needed modules
import os, socket, shutil, sys, datetime, platform, subprocess, configparser
from time import sleep

dt_now = datetime.datetime.now()
ptv = 0.1
settingsconfig = configparser.ConfigParser()
settingsconfig.add_section("settings")
settingsconfig.set("settings", "bootlog", "act")
settingsconfig.read("Settings/config.ini")
settings = settingsconfig["settings"]

ptver=1.0

#colors
def prRed(skk): print("\033[91m{}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m{}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m{}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m{}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m{}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m{}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m{}\033[00m" .format(skk))
def prBlack(skk): print("\033[98 {}\033[00m" .format(skk))

class bcolors: #2nd
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#reverse
class bg:
    black = '\033[40m'
    red = '\033[41m'
    green = '\033[42m'
    orange = '\033[43m'
    blue = '\033[44m'
    purple = '\033[45m'
    cyan = '\033[46m'
    lightgrey = '\033[47m'

reset = '\033[0m'

#definitions
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#get names
currentdir = os.path.basename(os.getcwd()) or "/"
username = os.getlogin()
hostname = socket.gethostname()
fullname = bcolors.OKGREEN+username+"@"+hostname+bcolors.ENDC+bcolors.WARNING+currentdir+bcolors.ENDC+" $ "


def pyterm():
    clear()
    print("Running PyTerm version: " + str(ptver))
    #appslist=os.listdir("Apps")
    commandexe=[]
    commandexe=[]
    erroslog=[]
    errors=0
    cmdcount=0

    while True:
        currentdir = os.path.basename(os.getcwd()) or "/"
        fullname = bcolors.OKGREEN+username+"@"+hostname+bcolors.ENDC+bcolors.WARNING+" "+currentdir+bcolors.ENDC+" $ "
        term=input(fullname)

        #pre made stuff to stop shit from breaking
        if "cd" in term:
            tmp = term.split()
            os.chdir(tmp[1])
        elif "exit" in term:
            quit()
        else:
            os.system(term)

if __name__ == "__main__":
    pyterm()
