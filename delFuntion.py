"""
crear un programa que informa del numero de datos recogidos luego pide al usuario los datos
que desea mantener en la lista empezando desde el primero y borrando el resto luego muestra al usuario 
la lista de los datos mantenidos y la lista original"""

datos = [1,2,3,4,5,6,7,8,9,0]

print("el numero de datos recogidos es de: ",len(datos),"datos")

n = int(input("cuantos datos deses mantener: "))

del datos[n: ]

print("los datos que estan en la lista son: ", datos)