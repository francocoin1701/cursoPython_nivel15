"""
inventario de una cajonera"""


cajonera = [
    [
        ["A",5],["B",9],["C",11],["D",41],["E",22],["F",35],["G",14],["H",44],["I",51],["K",21]
    ],
    [
        ["L",52],["M",14],["N",14],["Ñ",42],["O",25],["P",54],["Q",45],["R",25],["S",54],["T",1],["U",22],
        ["V",55],["W",47],["X",47],["Y",45],["Z",24]
    ]
]
print()
print("CAJONERA".center(50))

while True:
    print()
    print("1. Mostrar inventario")
    print("2. agregar cantidad de letra")
    print("3. vender cantidad de letra")
    print("4. salir")

    opcion = int(input("escoja una de las opciones del menu de arriba: "))

    if opcion == 1:
        for articulo in cajonera:
            for letra in articulo:
                print("letra: {}, cantidad: {} ".format(letra[0],letra[1]))

    elif opcion == 2:
        letr = input("escoje una letra ")
        canti = int(input("escoje la cantidad"))
        for articulo in cajonera:
            for letra in articulo:
                if letr.title() == letra[0]:
                    letra[1] -= canti          


    elif opcion == 3:
        letr = input("escoje una letra ")
        canti =int(input("escoje la cantidad que deseas agregar"))
        for articulo in cajonera:
            for letra in articulo:
                if letr.title() == letra[0]:
                    letra[1] += canti               


    elif opcion == 4:
        print("has salido del programa...")
        break 
    else:
        print("esa opcion no existe idiota no sea tan invesil buelva a intentarlo")               