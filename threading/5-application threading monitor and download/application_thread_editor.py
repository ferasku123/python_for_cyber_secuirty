import time
from threading import Thread,Lock
import os.path


def download_file(lock):
    global finsh
    for i in range(1,100):
        if os.listdir('folder'):
            print("warnning the folder is not empty")
        
        print("The file is begin to download",i)
        time.sleep(0.1)
    with lock:
        finsh = True

def isfolder_empty(lock):
    global finsh
    while(True):

        if  os.listdir('folder'):
           # print("Directory is not  empty")
            #the folder is not empty
            with open('file.txt','w') as f:
               f.write('warnning the folder is not empty')
            break
        with lock:
            if finsh:
                break

        
            

finsh = False
lock = Lock()

t1 = Thread(target=download_file,args=(lock,))
t2 = Thread(target=isfolder_empty,args=(lock,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done")


