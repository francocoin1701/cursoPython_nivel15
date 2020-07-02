import os
import random

palabras = ["CREADOR","GARBANZO","MURCIELAGO","ANTILOPE","MARIPOSA","TERMOMETRO",
            "DUQUEHIJODEPUTA","YURIBETAMBIEN","PEGAMENTO","CAFETERIA","CARNICERO","HERRAMIENTA","HOGUERA",
            "ASCENSOR","BELLOTA","CIRUJANO","CRUCIGRAMA"]


palabra = random.choice(palabras)

fallo0 = """
          !===N
              N    
              N
              N
       ========
"""
fallo1 = """
          !===N
          0   N    
              N
              N
       ========
"""      
fallo2 = """
          !===N
          0   N    
         /    N
              N
       ========
"""      
fallo3 = """
          !===N
          0   N    
         /|   N
              N
       ========
"""      
fallo4 = """
          !===N
          0   N    
         /|\  N
              N
       ========
"""      
fallo5 =  """
          !===N
          0   N    
         /|\  N
         /    N
       ========
"""      
fallo6 =  """
          !===N
          0   N    
         /|\  N
         / \  N
       ========
"""      
fallo7 =   """
          !===N
          0
          _   N    
         /|\  N
         / \  N
       ========
"""      

#are create three variabel by the game 

letras_correctas = ""
letras_toda = ""
fallos = 0

while True:
    os.system("cls")

    print("***************************")
    print("**** JUEGO DEL AHORCADO ***")
    print("***************************")

    if fallos == 0:
        print(fallo0)
    elif fallos == 1:
        print(fallo1)
    elif fallos == 2:
        print(fallo2)
    elif fallos == 3:
        print(fallo3)
    elif fallos == 4:
        print(fallo4)
    elif fallos == 5:
        print(fallo5)
    elif fallos == 6:
        print(fallo6)
    elif fallos == 7:
        print(fallo7) 

    print()


    #mostrando las letras acertadas y guiones bajos en las no acertadas

    resultado = ""

    for letra in palabra:
        if letra in letras_correctas:
            resultado += letra
        else:
            resultado += "_"  

    print("        {}".format(resultado))

    print()
    print()  

    #comprobamos si se ha haseptado la palabra o se han terminado los intentos

    if resultado == palabra:

        print("***** HAS GANADO *****")
        break
    if fallos > 7:
        print("la palabra era:",palabra)
        print("***** HAS PERDIDO *****")
        break

    while True:
        letra_usuario_sin_formato = input("dame una letra: ")
        letra_usuario = letra_usuario_sin_formato.upper()
        if len(letra_usuario) < 1 or len(letra_usuario)>1:
            print("introduce una letra")

        elif letra_usuario in letras_toda:
            print("esa letra ya existe")

        elif not letra_usuario.isalpha():
            print("Introduce solo letras no mumeros")

        else:
            letras_toda += letra_usuario
            break

        # comprobamos si la letra dicha por el usuario esta en la palabra

    if letra_usuario not in palabra:
        fallos += 1
    else:
        letras_correctas += letra_usuario              


