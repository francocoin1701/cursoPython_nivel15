#programa que nos diga cuantas vocales tiene una palabra que el usuario ingrese

palabra = input("ingrese una palabra: ")
vocales = "aeiou"
num_vocales = 0
contador = 0
num_consonantes = 0
consonantes = "bcdfghjklmnopqrstvwxyz"

while len(palabra) > contador:
    if palabra[contador] in vocales:
        num_vocales += 1
    elif palabra[contador] in consonantes:
        num_consonantes += 1
    contador += 1
print("la palabra tiene este numero de vocales: ", num_vocales)
print("la palabra tien este numero de consonantes: ",num_consonantes)    


