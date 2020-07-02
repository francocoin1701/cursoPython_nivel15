"""
Cinco amigos van a hacer una carrera:
Tomas, Maria, Laura, Miguel, Carlos
Muestra todos los posibles resultados que se pueden dar 
en la carrera"""

amigos = ["Tomas","Maria","Laura","Miguel","Carlos"]

Contador = 0

for i in amigos:
    for j in amigos:
        for k in amigos:
            for m in amigos:
                for n in amigos:
                    if i != j and i != k and i != m and i != n and \
                        j != k and j != m and j != n and \
                            k != m and k != n and m != n:

                            resultado = [i,j,k,m,n]
                            Contador += 1
                            print("{} : {}".format(Contador,resultado))
