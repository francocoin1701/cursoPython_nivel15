"""crear un programa que muestre por pantalla una cuenta regresiva
del 10 a el 0 utilizando el bucle for"""


#for i in range(10,-1,-1):
    #print(i)
#otra forma de haserlo
#for i in range(11):
   # print(10-i)

#programa que pide al usuario un numero que se sumara al de una lista dada y si el resultado de la suma es 100 entonses el usuario cumple la condicion y sale del programa


lista = [28,24,35,88,44,00,22,11,22,54,44,55,87]
numero = int(input("escriba un numero "))
prueva = True

for i in lista:
    if i + numero == 100:
        prueva = False

if prueva == False:
    print("haz ganado") 

else:
    print("perdiste")       
