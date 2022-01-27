import time
import threading

def calc_square(numbers):
   # print("calculate square numbers")
    for n in numbers:
       # time.sleep(1)
        #print('square:',n*n)
       sq.append(n*n)

def calc_cube(numbers):
    #print("calculate cube of numbers")
    for n in numbers:
        #time.sleep(1)
        #print('cube:',n*n*n)
        cu.append(n*n*n)
def calc_forth(numbers):
    for n in numbers:
        fo.append(n*n*n*n)


t = time.time()
arr = list(range(1,9000001))
sq = []
cu = []
fo = []


t1= threading.Thread(target=calc_square, args=(arr,))
t2= threading.Thread(target=calc_cube, args=(arr,))
t3 = threading.Thread(target=calc_forth,args=(arr,))

t1.start()
t2.start()
t3.start()

#t1.join()
#t2.join()
#t3.join()

print(sq[1])
print(cu[1])
print(fo[1])

print("done in : ",time.time()-t)
print("Hah... I am done with all my work now!")
