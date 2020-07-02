#comprobar cuantas veses aparese el caracter "o" con o sin tilde
#en la sighiente cadena de caracteres

cadena = "muchos años despues, frente al peloton de fucilamiento, el coronel aureliano buendia habia de recordar aquella tarde remota en que su padre lo llevo a conocer el hielo"

totalCadena = len(cadena)
n = 0
vocal_O = 0

while totalCadena > n:
    if cadena[n] == "o":
        vocal_O += 1
    n += 1

print("las veses que aparese la vocal o ", vocal_O)    
print(totalCadena)