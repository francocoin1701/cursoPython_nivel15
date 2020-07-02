#dada una lista y una variable comprovar si el valor de la variable se encuentra en que posicion de la lista esta utilizando el bucle for

lista = [14,25,27,52,49,85,68,54,51,43,86,58,67,84,91,44,12,24]

variable = 52

for i in range(len(lista)):
    if lista[i] == variable:
        print("esta en la pocicion ", i+1)