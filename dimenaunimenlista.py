"""
adgoritmo que permite pasar una lista unidimencional a una lista bidimencional
y vicebersa una lista bidimencional a una lista unidimensional.
"""

#lista uni dimencional a bidimencional
 
unidimencional = [1,2,3,4,5,6,7,8,9,0]
unidimencional2 = ["a","b","c","d","e","f","g","h","i","j"]
bidimencional = []

for algo in range(len(unidimencional)):
    bidimencional.append([unidimencional[algo],unidimencional2[algo]])
print(bidimencional)

#lista bidimencional a unidimencional

listabidimencional = [
    [1, 'a'], [2, 'b'], [3, 'c'], [4, 'd'], 
    [5, 'e'], [6, 'f'], [7, 'g'], [8, 'h'], 
    [9, 'i'], [0, 'j']
]

numeros = []
letras = []

for i in listabidimencional:
    numeros.append(i[0])
    letras.append(i[1])

print(letras)
print(numeros)    

