import time

def calc_square(numbers):
    #print("calculate square numbers")
    for n in numbers:
       # time.sleep(1)
      #  print('square:',n*n)
        sq.append(n*n)

def calc_cube(numbers):
    #print("calculate cube of numbers")
    for n in numbers:
    
        cu.append(n*n*n)

def calc_fourth(numbers):
    for n in numbers:
        fo.append(n*n*n*n)

t = time.time()
arr = list(range(1,9000001))
sq = []
cu = []
fo = []

calc_square(arr)
calc_cube(arr)
calc_fourth(arr)

print(sq[1])
print(cu[1])
print(fo[1])

print("done in : ",time.time()-t)
print("Hah... I am done with all my work now!")
