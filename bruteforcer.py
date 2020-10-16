from __future__ import print_function
import requests;import termcolor;from termcolor import colored;import warnings
import core,Proxy
import time;from time import sleep;import sys; import argparse;from argparse import ArgumentParser
warnings.filterwarnings('ignore')
__banner__ = """
                |     | |```` |```)     |````  / ```\   |````)   /````  |````  |````)
                |  |  | |~~~~ |**)      |~~~  |  /  |   |--\*   |       |~~~   |--\*
                |__|__| |____ |___)     |      \___/    |   \    \ __   |___   |   \ 


                        
                        Author : Tekchand
                        Description : Not Responsible for Any damage to the server
                        Created: 21/7/2020
            """
print(__banner__)
head={
        'User-Agent':'Mozilla/5.0(Window NT 100; ...)Gecko/20100101 Firefox/77.0',
        'Content-Type':'text/html',
        'Connection':'close',
        'Accept': '/'

    }

def Requester(j,passer,ext,proxyhandle):
    try:
        Requester.remote=requests.get(str(argumenthandler().url)+"/%s%s" % (str(j),str(ext)),headers=head,verify=False,allow_redirects=False,proxies=proxyhandle)
        if Requester.remote.status_code == 200:
            sys.stdout.write(str(colored("%s [+] %s  => %s/%s%s\r\n" % (time.ctime(),passer,str(argumenthandler().url),str(j),str(ext)),"green",attrs=['bold'])))
            sys.stdout.flush()
        elif Requester.remote.status_code == 302:
            sys.stdout.write(str(colored("%s [*]Redirect => %s/%s%s\r\n" % (time.ctime(),str(argumenthandler().url),str(j),str(ext)),"yellow",attrs=['bold'])))
            sys.stdout.flush()
        elif Requester.remote.status_code == 404:
            sys.stdout.write(str(colored("%s [-] Not Found => %s/%s%s\r" % (time.ctime(),str(argumenthandler().url),str(j),str(ext)),"red",attrs=['bold'])))
            sys.stdout.flush()
        elif Requester.remote.status_code == 500:
            sys.stdout.write(str(colored("%s [~] Internal Server Error => %s/%s%s\r" % (time.ctime(),str(argumenthandler().url),str(j),str(ext)),"white",attrs=['bold'])))
            sys.stdout.flush()
        elif Requester.remote.status_code == 400:
            sys.stdout.write(str(colored("%s [~] Bad request => %s/%s%s\r" % (time.ctime(),str(argumenthandler().url),str(j),str(ext)),"white",attrs=['bold'])))
            sys.stdout.flush()
        elif Requester.remote.status_code == 403:
            sys.stdout.write(str(colored("%s [!] Forbidden => %s/%s%s\r\n" % (time.ctime(),str(argumenthandler().url),str(j),str(ext)),"blue",attrs=['bold'])))
            sys.stdout.flush()
        elif Requester.remote.status_code == 503:
            sys.stdout.write(str(colored("%s [-] Server Unavailable  => %s/%s%s\r" % (time.ctime(),str(argumenthandler().url),str(j),str(ext)),"magenta",attrs=['bold'])))
            sys.stdout.flush()
        else:
            pass
    except requests.exceptions.ConnectionError as req:
        print(termcolor.colored("[-]Retrying Connection to the server...","red",attrs=['bold']))

proxydata={}
with open("db/proxy.txt","rb") as qe:
    for h in qe.readlines():
        proxydata[h]=8080

def repeater(j):
    try:
        if argumenthandler().wordlist:
            Requester(j,"Found",argumenthandler().extension,None)
        elif argumenthandler().path:
            Requester(j,"Admin Found",None,None)
        elif argumenthandler().proxy and argumenthandler().wordlist:
            for x,y in proxydata.items():
                print("hacked")
                Requester(j,"Found",argumenthandler().extension,"{'%s':'%s'}" % (x,y))
        elif argumenthandler().proxy and argumenthandler().path:
            for x,y in proxydata.items():
                Requester(j,"Admin Found",None,"{%s:%s}" % (x,y))
        else:
            print("please provide proper argument")
            sys.exit(1)

    except Exception as yu:
        sys.exit(1)

if __name__ == "__main__":

    def argumenthandler():
        arghandle=ArgumentParser(description=termcolor.colored("Directory Brute Forcer","green",attrs=['bold']))
        arghandle.add_argument("--url",action="store",dest="url",help="URL of the website")
        arghandle.add_argument("--wordlist",action="store",dest="wordlist",help="Path of wordlist to brute force")
        arghandle.add_argument("--extension",action="store",dest="extension",help="Specify Extension like (php.asp,aspx.jsp,js,html) only for directory brute force")
        arghandle.add_argument("--threads",action="store",dest="threads",help="Maximum number of thread Recommended 100 or max")
        arghandle.add_argument("--pannel",action="store",dest="pannel",help="Admin Pannel Found of Website")
        arghandle.add_argument("--path",action="store",dest="path",help="Wordlist Only Using on Admin pannel")
        arghandle.add_argument("--version",action="store_const",const="version",dest="version",help="Show version of program and exit")
        arghandle.add_argument("--proxy",action="store_const",const="proxy",dest="proxy",help="Use Proxy Server For Safe during Attack but Slow")
        makertest=arghandle.parse_args()
        return makertest

    PRINTER="[*]Brute force starting"

    try:
        if argumenthandler().url and (argumenthandler().extension or not argumenthandler().extension) and argumenthandler().threads and argumenthandler().wordlist and (argumenthandler().proxy or not argumenthandler().proxy):
            print(PRINTER)
            core.Threadhandler(argumenthandler().wordlist,argumenthandler().threads,repeater)
        elif argumenthandler().version:
            print("Stable release 1.0.1")
            sys.exit(1)
        elif argumenthandler().url and argumenthandler().threads and (argumenthandler().extension or not argumenthandler().extension) and argumenthandler().path:
            print(PRINTER)
            print("[*]Targetting applied on admin pannel")
            
            core.Threadhandler(argumenthandler().path,argumenthandler().threads,repeater)

        elif argumenthandler().url and argumenthandler().threads and argumenthandler().threads and argumenthandler().pannel and (argumenthandler().extension or not argumenthandler().extension()):
            repeater()

        else:
            argumenthandler()
            sys.exit(1)
    except Exception as eee:
        print(eee)
