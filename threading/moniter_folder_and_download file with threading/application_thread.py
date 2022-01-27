import time
import threading
import os.path

def download_file():
    for i in range(1,100):
        if os.listdir('folder'):
            print("warnning the folder is not empty")
        
        print("The file is begin to download",i)
        time.sleep(0.1)

def isfolder_empty():
    while(True):

        if  os.listdir('folder'):
           # print("Directory is not  empty")
            #the folder is not empty
            with open('file.txt','w') as f:
               f.write('warnning the folder is not empty')
            break
        
            



t1 = threading.Thread(target=download_file)
t2 = threading.Thread(target=isfolder_empty)

t1.start()
t2.start()

t1.join()
t2.join()

print("done")


