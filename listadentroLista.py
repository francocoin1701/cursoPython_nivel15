"""
en una tienda quieren haser un inventario de las figuras que tienen y el numero de identidad de cada una
crea una lista que tinga las unidades del inventario :
3 cuadrados, 5 triangulos, 8 rectangulos, 4 octaedros."""

figuras = [[3, "cuadrados",[1,3]],
          [5, "triangulos",[3,9]],
          [8, "rectangulos",[2,8]],
          [4, "octaedros",[2,6]]]

for figura in figuras:
    print(" cantidad: {} ariticulo: {} fila: {} columna: {} ".format(figura[0],figura[1],figura[2][0],figura[2][1]))          