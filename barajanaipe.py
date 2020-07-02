# crear una baraja de naipes donde le devuelba al usuario una baraja ordenada
import random
tantos = ["A","2","3","4","5","6","7","s","c","r"]
palos = ["oros","copas","espadas","bastos"]
baraja = []

for t in tantos:
    for p in palos:
        carta = "{} de {}".format(t,p)
        baraja.append(carta)

random.shuffle(baraja)
for i in range(0,40,4):
    for carta in range(4):
        print(" {:14} ".format(baraja[i+carta]),end=" ")
    print()
print()    

#repartiendo cartas con el uso del metodo pop
"""jugador1 = []
jugador2 = []
jugador3 = []
jugador4 = []

for i in range(5):
    carta1 = baraja.pop(0)
    jugador1.append(carta1)
    carta2 = baraja.pop(0)
    jugador2.append(carta2)
    carta3 = baraja.pop(0)
    jugador3.append(carta3)
    carta4 = baraja.pop(0)
    jugador4.append(carta4)"""

"""otra forma de codificar el reparto de las cartas puede ser:"""

jugadores = [[],[],[],[]]
for i in range(4):
    for j in range(5):
        jugadores[i].append(baraja.pop(0))


#barajando las cartas
jugadore = [list(jugadores[0]),list(jugadores[1]),list(jugadores[2]),list(jugadores[3])]

#mostrando las cartas al jugador

for i in range(len(jugadore)):
    print("jugador {} :".format(i+1))
    for j in range(5):
        print("{:14}".format(jugadore[i][j]),end="")
    print()     
print()


#mostrando las cartas restantes

for i in range(0,20,4):
    for j in range(4):
        print("{:14} ".format(baraja[i+j]),end=" ")
    print()

    
          
