#crear una tupla apartir de las tres dadas la tupla creada debera contener las mascotas

mamiferos = ("tigre", "gato", "leon")
aves = ("aguila", "buitre", "canario")
reptiles = ("tortuga", "serpiente")

mascotas = mamiferos[1:2] + aves[2:] + reptiles[:1]

print(mascotas)

print(aves[1])