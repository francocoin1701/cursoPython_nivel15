#programa que pide al usuario adivinar un numero de el 1 a el 100 dandole 7 intentos e indicandole si esta por ensima o por abajo de el numero luego de cada intento para guiarlo

import random

numero = random.randint(1,100)

vandera = True

intentos = 0

print("ADIVINA EL NUMERO QUE ESTA EN EL RANGO DE EL 1 AL 100")

while vandera:
    intentos += 1
    
    if intentos <= 7:
        num = int(input("dame un numero: "))
        if num == numero:
          print("haz conseguido el numero requerido en ",intentos,"intentos")
          vandera = False

        elif num > numero:
          print("el numero que buscas es menor llevas",intentos,"intentos")
        elif num < numero:
          print("el numero que buscas es mayor llevas",intentos,"intentos") 
    else:
        print("perdiste gastastes todos los intentos llevas",intentos)
        vandera = False
