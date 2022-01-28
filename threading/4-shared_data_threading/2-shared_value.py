from threading import Thread,Lock
import time

def increase(lock):
    global db_value
    with lock:
        local_value = db_value

        local_value = local_value +1
        time.sleep(0.3)
        db_value = local_value

lock = Lock()
db_value = 0
print('start value: ',db_value)

t1 = Thread(target=increase,args=(lock,))
t2 = Thread(target=increase,args=(lock,))

t1.start()
t2.start()

t1.join()
t2.join()

print("end value: ",db_value)
print("end main")


