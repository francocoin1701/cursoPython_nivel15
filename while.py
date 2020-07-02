num = 5
voc = "a"


puntos = 100
vandera = True

while vandera:
    numero = int(input("escribe un numero de 1 a 5"))
    vocal = input("escriba una vocal")
    if numero != num and vocal != voc:
        puntos -= 5 
        print("te quedan puntos ", puntos)    

    elif numero != num or vocal != voc:
        puntos -= 2
        print("te quedan puntos ", puntos)
    else:
        vandera = False
        print("acertaste")    
