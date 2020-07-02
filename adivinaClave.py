"""
programa que adivina una clave mediante fuerza bruta
la clave consiste en 4 letras minusculas"""

import time

clave = input("inserta una clave: ")

alfabeto = "abcdefghijklmnñopqrstuvwyz"

inicio = time.time()

for c1 in alfabeto:
    for c2 in alfabeto:
        for c3 in alfabeto:
            for c4 in alfabeto:
                for c5 in alfabeto:
                    intento = c1+c2+c3+c4
                    if intento == clave:
                        print("encontraste la clave y es: ",intento)
final = time.time()
print("esto se tardo: ",final - inicio)

