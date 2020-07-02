#realizar un programa que pida un numero al usuario y que le muestre las tablas de multiplicar de el numero que el usuario muestra

num = int(input("dame un numero: "))

for i in range(1,11):
    print(num ,"*", i, "=", i*num)