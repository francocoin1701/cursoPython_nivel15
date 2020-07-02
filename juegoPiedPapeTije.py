#crear un juego de piedra papel o tijera y que permita la opcion al jugador de decidir si quiere seguir jugando luego de cada iteraccion con el juego

import random


vandera = True

while vandera:
    print("juego de piedra papel o tijera")
    ordenador = random.choice(["piedra","papel","tijeras"])
    jugador = input("escoje si piedra papel o tijeras")
   


    if jugador == "piedra":
        if ordenador == "piedra":
            print("has empatado el ordenador saco",ordenador)
        elif ordenador == "papel":
            print("has perdido el ordenador saco",ordenador)

        elif ordenador == "tijeras":
            print ("has ganado el ordenador saco ",ordenador)    
    elif jugador == "papel":
        if ordenador == "papel":
            print("has empatado el ordenador saco",ordenador)
        elif ordenador == "tijeras":
            print("has perdido el ordenador saco",ordenador)

        elif ordenador == "piedra":
            print ("has ganado el ordenador saco ",ordenador) 

    elif jugador == "tijeras":
        if ordenador == "tijeras":
            print("has empatado el ordenador saco",ordenador)
        elif ordenador == "piedra":
            print("has perdido el ordenador saco",ordenador)

        elif ordenador == "papel":
            print ("has ganado el ordenador saco ",ordenador)  
    else:
        print("esa opcion no existe pendejo")  

    seguir = ""                 
    while seguir != "n" or seguir != "s":
        seguir = input("quiere seguir jugando s/n")
        if seguir == "s":
            break
        elif seguir == "n":
            vandera = False
            break
        else:
            print("esa obcion no existe idiota")    

