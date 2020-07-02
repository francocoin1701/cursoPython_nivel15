import time

inicio = time.time()
for i in range(11):
    for j in range(10):
        for f in range(10):
            print("{} {} {} ".format(i,j,f))

final = time.time()
print("el adgoritmo tardo: ",final-inicio)            