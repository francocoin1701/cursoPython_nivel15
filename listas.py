#crear una lista que contenga los numeros de 1 a 100 utilizando el bucle while y partiendo de una lista basia

lista = []
contador = 1

while contador <= 100:
    lista = lista + [contador]
    contador += 1

print(lista)


#programa que nos pide adivinar 5 colores si adivinas los colores tedara 1 punto por color

colores = ["verde", "rojo", "amarillo", "negro", "morado"]

puntaje = 0

vandera = True

while vandera:
    color = input("escribe un color: ")

    if color in colores:
        puntaje += 1
        print("el puntaje que llevas es de: ",puntaje)
        
    else: 
        print("perdiste tu puntaje es de: ",puntaje)
        vandera = False    


    