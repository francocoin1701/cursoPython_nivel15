#aplanar una lista anidada utilizando el bucle for teniendo en cuenta los diferentes tipos de datos que se encuentran en la lista a aplanar

datos = [1,5,8,2,[1,5,6,7,],[1,[4,2,5,7,]]]

plana = []

for dato in datos:
    if type(dato) == int:
        plana.append(dato)

    elif type(dato) == list:
        for elemento in dato:
            if type(elemento) == int:
                plana.append(elemento)

            elif type(elemento) == list:
                for objet in elemento:
                    plana.append(objet)        

print(plana)
print(datos)                    