#crear un programa que permita un conteo regresivo de 10 segundos y que muestre por pantalla el conteo de 10 a 0 y tambien el tiempo que tomo en ejecutar este programa

import time

inicio = time.time()

for i in range(11):
    print(10-i)
    time.sleep(1)

final = time.time()

print("el tiempo que se tomo en ejecutar el programa fue de :",final-inicio-1)