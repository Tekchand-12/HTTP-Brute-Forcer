import socket
import time; from time import sleep
import threading
import re
import ssl
import sys

class Server:
    def __init__(self):
        pass

    def Connection(self):
        self.handler=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.handler.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.handler.bind(("127.0.0.1",8080))
        self.handler.listen(10)

    def counter(self):
        while True:
            self.c,self.addr=self.handler.accept()
            self.last=threading.Thread(target=self.acceptor,args=())
            self.last.setDaemon(True)
            self.last.start()
            #self.last.join()
            sleep(1)
    
    def acceptor(self):
        result=self.c.recv(5000)
        while True:
            portfinder=str(re.findall("^[A-Z].*HTTP.*",result))
        
            global httport
            if re.findall("http",portfinder):
                httport=80
            elif re.findall("https",portfinder):
                httport=443
            else:
                httport=80

            hostfinder=str(str(str(re.findall("Host.*[com|org|in|io]",result)).replace(']','')).replace('[','')).replace("'",'')
            finalhost=str(str(hostfinder[5:50]).strip()) 
            print "Receiving 127.0.0.1 <---%s" % (str(self.addr))
            self.serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.serversocket.connect((finalhost,httport))
            self.serversocket.sendall(result)
            print "Sending 127.0.0.1 ---> %s" % (str(self.serversocket.getpeername()))

            while True:
                toclient=self.serversocket.recv(1024)
                print  "Receiving response 127.0.0.1 <--- %s" % (str(self.serversocket.getpeername()))
                self.c.send(toclient)
	        print "Sending data 127.0.0.1 ---->%s" % (str(self.addr))
                #self.serversocket.close()

        else:
            print "not received"
            sys.exit(1)

     
if __name__ == "__main__":
    print "[*]proxy server started"
    f=Server()
    f.Connection()
    f.counter()


