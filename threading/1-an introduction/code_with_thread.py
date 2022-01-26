
import time
import threading

def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(1)
        print('square:',n*n)

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(3)
        print('cube:',n*n*n)

arr = [2,3,8,9]

t = time.time()

t1= threading.Thread(target=calc_square, args=(arr,))
t2= threading.Thread(target=calc_cube, args=(arr,))
print("ready")
print("threading is start")
t1.start()
t2.start()

print("\nhello world")
print("you are in threading time")

t1.join()
t2.join()

print("done in : ",time.time()-t)
print("Hah... I am done with all my work now!")
