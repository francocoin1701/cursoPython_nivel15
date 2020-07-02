"""
para un juego que va a tener 20.000 planetas necesitamos formar nombres
para cada uno de los planetas.Cres una lista con todos los posibles nombres de 3 silavas
que se pueden formar con 10 consonantes y 5 vocales, de tal forma que cada letra sea seguida
de una vocal y no se repita ninguna letra en cada uno de los nombres
al final se mostrara 10 nombres de la lista a la zar y la cantidad de nombres que resultaron de este ejercicio
"""

import random

consonantes = "cdbfljgtrkzq"
vocales = "aeiou"

nombres = []

for c1 in consonantes:
    for v1 in vocales:
        for c2 in consonantes:
            for v2 in vocales:
                for c3 in consonantes:
                    for v3 in vocales:
                        if c1 != c2 and c1 != c3 and c2 != c3 and \
                            v1 != v2 and v1 != v3 and v2 != v3:

                                nombre = c1+v1+c2+v2+c3+v3
                                nombres.append(nombre) 
print("cantidad de nombres: {}".format(len(nombres)))

for i in range(1,11): 
    planeta = random.choice(nombres)
    print("nombre de el planeta: {} : {} ".format(i,planeta))
