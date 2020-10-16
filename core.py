import threading;import Queue;import termcolor;import sys
from threading import Lock

data=[]
outtest=[]

def Threadhandler(wordtest,threads,reptfunction):
    with open(str(wordtest),'rb') as fp:
        for i in fp.readlines():
            data.append(str(i).replace('\n',''))

    waiter=Lock()
    makes=set()
    stack=Queue.PriorityQueue(maxsize=len(data))
    for poster in data:
        stack.put_nowait(poster)
    try:
        while stack.empty()!=True:
            for r in range(0,int(threads)):
                msfhandler=threading.Thread(target=reptfunction,args=(stack.get_nowait(),))
                makes.add(msfhandler)
                msfhandler.daemon=False
            waiter.acquire()
            for t in makes:
                t.start()
            waiter.release()
            waiter.acquire()
            for msf in makes:
                msf.join()
            outtest.extend(makes)
            makes.clear()
            waiter.release()
    except KeyboardInterrupt as pp:
        print termcolor.colored("[-] Operation Canceled by User","red",attrs=['bold'])
        sys.stderr.flush()
        sys.exit(1)
    except Queue.Empty as retest:
        pass
        print "\n"
        print "[*] Brute Force Complete"
    return 
