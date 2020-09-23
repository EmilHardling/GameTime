import time
import math
from binTreeFile import Bintree

def internet():
    lower = 0
    upper = 10000
    sum = 0
    prime = []
    print("Prime numbers between", lower, "and", upper, "are:")

    for num in range(lower, upper + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                sum += num
    print("Internet upp till", upper)
    print(sum)
def egen():
    summa = 2
    primelist = [2]
    lower = 3
    upper = 100000
    sum = 2
    for num in range(lower,upper+1,2):
        #if num%2 == 0:
            #num += 1
        for i in primelist:
            if (num%i)== 0:
                    break
        else:

            primelist.append(num)
            summa += num
    #print(primelist)
    return summa
start_time = time.time()
internet()
tid1 =(time.time() - start_time)
print(tid1,"sekunder")
tidtabel = []
for k in range(10):
    start_time = time.time()
    summa = egen()
    tid2 =(time.time() - start_time)
    tidtabel.append(tid2)
print("---------------------------------------")
print(summa)
print((sum(tidtabel)/len(tidtabel)),"sekunder")
print("---------------------------------------")
print("skillnad mellan internet/egen",int((tid1/tid2)*100),"%")
