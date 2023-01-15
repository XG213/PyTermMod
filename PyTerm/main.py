#PyTerm, a simple terminal write with python

#needed modules
import os, socket, shutil, sys, datetime, platform, subprocess, configparser
from time import sleep

nilpath = os.path.abspath(__file__)
path = os.path.dirname(nilpath)
dt_now = datetime.datetime.now()
ptv = 0.1
settingsconfig = configparser.ConfigParser()
settingsconfig.add_section("settings")
settingsconfig.set("settings", "bootlog", "act")
settingsconfig.read("Settings/config.ini")
settings = settingsconfig["settings"]

bootlog = settings["bootlog"]
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
def shutdown(): print(quit())
def getlogin(): os.getlogin()
def gethostname(): socket.gethostname()
def getip():
    ip = socket.gethostbyname(hostname)
    print(ip)
def getinfo():
    print("computer name: "+os.getlogin())
    print("host name: "+socket.gethostname())
    print("IP address: "+socket.gethostbyname(hostname))
    print("python version: "+platform.python_version())

def getpythonversrion():
    pyv = platform.python_version()
    print(pyv)

def getpath(): print(path)
def printdir():
    dirlist = os.listdir(path)
    print(dirlist)


def shutdownhost(): os.system("shutdown /s /t 1")
def makedir(): os.mkdir(pyterm.mkdir)
def clear(): os.system('cls')
def pause(): pauseint=input("press enter to countuine . . .")
def openfile(): subprocess.Popen(pyterm.op)
def ffcheck():
    prYellow("Checking folders")
    print("Settings")
    if os.path.exists("Settings"):
        prGreen("status: checked")
    else:
        prRed("folder not fount")
        prYellow("sending request")
        shutdown()
    prYellow("checking files")
    print("config.ini")
    if os.path.exists("Settings/config.ini"):
        prGreen("status: checked")
    else: 
        prRed("file not found")
        prYellow("sending request")
        shutdown()
    prYellow("Warning! you disactivate bootlog manually on config.ini>bootlog change to dis or doing the command 'term -dis bootlog' in the terminal")
def bootlogdef():
    clear()
    osplatform = sys.platform
    getpythonversrion()
    print("Using", osplatform)
    print("access:", dt_now)
    sleep(2)
    ffcheck()
    sleep(1)
    clear()
    
#get names
username = os.getlogin()
hostname = socket.gethostname()
fullname = bcolors.OKGREEN+username+"@"+hostname+bcolors.ENDC+bcolors.WARNING+" ~"+bcolors.ENDC+" $ "
fullpip = bcolors.OKGREEN+username+"@"+hostname+bcolors.ENDC+bcolors.OKBLUE+"/pip"+bcolors.ENDC+bcolors.WARNING+" ~"+bcolors.ENDC+" $ "
fullcmd = bcolors.OKGREEN+username+"@"+hostname+bcolors.ENDC+bcolors.OKBLUE+"/cmd"+bcolors.ENDC+bcolors.WARNING+" ~"+bcolors.ENDC+" $ "
fullecho = bcolors.OKGREEN+username+"@"+hostname+bcolors.ENDC+bcolors.OKBLUE+"/echo"+bcolors.ENDC+bcolors.WARNING+" ~"+bcolors.ENDC+" $ "


def pyterm():
    clear()
    #appslist=os.listdir("Apps")
    commandexe=[]
    cmdslist=["get username", "get hostname", "get pythonversion", "clear", "help", "pause", "make dir", "del dir", "dir", "shutdown", "get path", "pip install", "pip uninstall", "make file", "del file", "pip list", "run pip", "pip", "term --version", "get info", "shutdown host", "open", "run cmd", "term", "term -dis bootlog", "echo", "get cmdlog", "get errorscount", "get cmdcount", "", " ", "get errorslog", "term -act bootlog", "get ip", "python3"]
    commandexe=[]
    erroslog=[]
    errors=0
    cmdcount=0

    while True:
        term=input(fullname)

        #check if user input a wrong command

        if term.__contains__("pip install"):
            commandexe.append(term)
            cmdcount = cmdcount +1
            revpipinst = term.replace("pip install ", "")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', revpipinst])
            prGreen("installed "+revpipinst)

        elif term.__contains__("pip uninstall"):
            commandexe.append(term)
            cmdcount = cmdcount +1
            revpipuninst = term.replace("pip uninstall ", "")
            subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', revpipuninst])
            prGreen("uninstalled "+revpipinst)
        
        elif term.__contains__("make dir"):
            commandexe.append(term)
            cmdcount = cmdcount +1
            revmkdir = term.replace("make dir ", "")
            os.mkdir(revmkdir)
            prGreen("Created "+revmkdir)
        
        elif term.__contains__("del dir"):
            commandexe.append(term)
            cmdcount = cmdcount +1
            revdeldir = term.replace("del dir ", "")
            os.rmdir(revdeldir)
            prGreen("Deleted "+revdeldir)

        elif term.__contains__("make file"):
            commandexe.append(term)
            cmdcount = cmdcount +1
            revmkfile = term.replace("make file ", "")
            prYellow("Creating "+revmkfile)
            mkfile = open(revmkfile, "w")
            prGreen("Created "+revmkfile)

        elif term.__contains__("del file"):
            commandexe.append(term)
            cmdcount = cmdcount +1
            revdelfile = term.replace("del file ", "")
            prYellow("Deleting "+revdelfile)
            os.remove(revdelfile)
            prGreen("Deleted "+revdelfile)

        elif term.__contains__("echo"):
            commandexe.append(term)
            cmdcount = cmdcount +1
            revecho = term.replace("echo ", "")
            print(revecho)

        elif term.__contains__("open"):
            commandexe.append(term)
            cmdcount = cmdcount +1
            revopen = term.replace("open ", "")
            prYellow("opening "+revopen)
            os.startfile(revopen)

#########################################################
        elif term not in cmdslist:
            prRed(term+" : Not A Valid Command")
            erroslog.append(term)
            errors = errors +1


        #get pc username    
        elif term=="get username":
            commandexe.append("get username")
            cmdcount = cmdcount +1
            print(username)

        #print all commands exe
        elif term=="get cmdlog":
            commandexe.append("get commandlog")
            cmdcount = cmdcount +1
            print(commandexe)


        #prints count of erros
        elif term=="get errorscount":
            commandexe.append("get errorscount")
            cmdcount = cmdcount +1
            print(errors)

        
        elif term=="help":
            print("""
PyTerm
A terminal writen all in python

GitHub: https://github.com/totallynotdrait/PyTerm

If theres any issues with PyTerm, you can consult the GitHub reposity\nand have more infomartion about it

Thanks for using PyTerm!

            """)



        #prints cmd count
        elif term=="get cmdcount":
            commandexe.append("get cmdcount")
            cmdcount = cmdcount +1
            print(cmdcount)

            
        #prints cmd count
        elif term=="get errorslog":
            commandexe.append("get errorslog")
            cmdcount = cmdcount +1
            print(erroslog)

        #get pc hostname
        elif term=="get hostname":
            commandexe.append("get hostname")
            cmdcount = cmdcount +1
            print(hostname)


        #get python version
        elif term=="get pythonversion":
            commandexe.append("get pythonversion")
            cmdcount = cmdcount +1
            getpythonversrion()


        #print the current path is the user
        elif term=="get path":
            commandexe.append("get path")
            cmdcount = cmdcount +1
            getpath()


        #gets user ip
        elif term=="get ip":
            commandexe.append("get ip")
            cmdcount = cmdcount +1
            getip()


        #gets user info
        elif term=="get info":
            commandexe.append("get info")
            cmdcount = cmdcount +1
            getinfo()

        #gets info about pip
        elif term=="pip":
            commandexe.append("pip")
            cmdcount = cmdcount +1
            subprocess.check_call([sys.executable, '-m', 'pip'])

        #runs pip
        elif term=="run pip":
            commandexe.append("run pip")
            cmdcount = cmdcount +1
            prRed(term+" : Command Not Avaible At This Time")
            #pip=input(fullpip)
            #subprocess.check_call([sys.executable, '-m', pip])
                

        #get the list of alll python packages the user installed
        elif term=="pip list":
            commandexe.append("pip list")
            cmdcount = cmdcount +1
            subprocess.check_call([sys.executable, '-m', 'pip', 'list'])

        
        #run command prompt
        elif term=="run cmd":
            commandexe.append("run cmd")
            cmdcount = cmdcount +1
            while True:
                cmd=input(fullcmd)
                if cmd=="exit":
                    break
                os.system(cmd)

        #clears any prints and inputs
        elif term=="clear":
            commandexe.append("clear")
            cmdcount = cmdcount +1
            clear()


        #does a pause
        elif term=="pause":
            commandexe.append("pause")
            cmdcount = cmdcount +1
            pause()

        #prints all files and folders that are in the current directory
        elif term=="dir":
            commandexe.append("dir")
            cmdcount = cmdcount +1
            printdir()
        
        
        #exits the script
        elif term=="shutdown":
            commandexe.append("shutdown")
            cmdcount = cmdcount +1
            prYellow("sending request")
            shutdown()
        

        #opens a file or app
        elif term=="open":
            commandexe.append("open")
            cmdcount = cmdcount +1
            op=input("input path of the app to open: ")
            openfile()


        #shutdown your computer
        elif term=="shutdown host":
            commandexe.append("shutdown host")
            cmdcount = cmdcount +1
            prYellow("sending request")
            shutdownhost()


        #disactivate bootlog
        elif term=="term -dis bootlog":
            editbootlog = settingsconfig["settings"]
            editbootlog["bootlog"] = "dis"

            with open("Settings/config.ini", "w") as bl:
                settingsconfig.write(bl)
                prGreen("disactivated bootlog")

        
        elif term=="term -act bootlog":
            editbootlog = settingsconfig["settings"]
            editbootlog["bootlog"] = "act"

            with open("Settings/config.ini", "w") as bl:
                settingsconfig.write(bl)
                prGreen("activated bootlog")

        elif term=="term":
            print("\nusage:")
            print(" term <command> [options]")
            print("\ncommands:")
            print(" -act            Activates a option")
            print(" -dis            Disactivates a option")
            print("\n")
            print("options:")
            print(" bootlog         Prints information and check files and folders if does exists")

        elif term=="term --version":
            print(ptver)

        elif term=="python3":
            prYellow("sending request")
            sleep(1)
            clear()
            os.system("python")


            





#get info
if settings["bootlog"] == "act":
    bootlogdef()
    pyterm()
else:
    pyterm()

