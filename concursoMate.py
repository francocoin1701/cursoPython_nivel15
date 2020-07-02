# programa que genere operaciones matematicas al azar y le pida al usuario resolverlas y luego de 10 segundos el programa se detenga. Por cada asierto el usuario obtendra un punto al final de el juego se le mostrara al usuario su puntaje


import time
import random

input("oprima enter para iniciar el juego")
puntaje = 0

comienzo = time.time()

while True:
    n1 = random.randint(0,9)
    n2 = random.randint(0,9)

    sI = random.choice(["*","+"])

    if sI == "*":
        resultado = n1 * n2
        print(n1, sI, n2,end=" ")
    elif sI == "+":
        resultado = n1 + n2
        print(n1,sI,n2,end=" ")    

    respuesta = int(input("= "))

    if respuesta == resultado:
        puntaje += 1
        print("es correcto llevas",puntaje,"puntos")
    else:
        print("no es correcto llevas estos",puntaje,"puntos")

    final = time.time()

    if final - comienzo >= 15:
        print("se acabo el juego")
        break
print("juego terminado")
print("tu puntaje es de: ",puntaje)    




