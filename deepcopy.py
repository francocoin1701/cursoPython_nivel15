"""
en este programa mostramos la forma en como podemos haser una copia
de una lista que tiene mas listas como elementos de forma que se pueda 
modificar la copia de la list sin tener que modificar la original.
"""

#primer forma de como podemos llevar a cabo el ejercicio

p = [1,[2,3],[3,4,6]]

q = [p[0],list(p[1]),list(p[2])]

p[2][0]=15
print(p)
print(q)

#comprobamos que el espacio en memoria donde estan guardadas las variables sean diferentes

print(id(p))
print(id(q))

"""segundo forma para haser el ejercicio"""

p = [3,[2,5],[2,[3,5]]]
q = [p[0]]+[list(p[1])]+[list(p[2])]

p[2][1][0]=5
print(p)
print(q)
print(id(p))
print(id(q))



