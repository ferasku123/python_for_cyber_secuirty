from threading import Thread
import time

def increase():
    global db_value
    local_value = db_value

    local_value = local_value +1
    time.sleep(0.3)
    db_value = local_value

db_value = 0
print('start value: ',db_value)

t1 = Thread(target=increase)
t2 = Thread(target=increase)

t1.start()
t2.start()

t1.join()
t2.join()

print("end value: ",db_value)
print("end main")


