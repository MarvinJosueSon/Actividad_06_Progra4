productos = {}
def Ingreso():
    cantidad=int(input("Ingrese cuantos productos quiere agregar: "))
    i=1
    while i <= cantidad:
        try:
            auxCodigo = input("Ingrese el codigo del producto: ")
            if auxCodigo not in productos:
                print("El codigo del producto ya existe")
            else:
                nombreAux=input("Ingrese el nombre del producto: ")
                categoriaAux=input("Ingrese el categoria del producto: (hombre, mujer, niños, otros)").lower()
                tallaAux=input("Ingrese el talla del producto: ")
                precioAux=float(input("Ingrese el precio del producto: "))
                stockAux=int(input("Ingrese el stock del producto: "))
                if stockAux>0 and precioAux>0:
                    if categoriaAux == "mujer" or categoriaAux == "hombre" or categoriaAux == "niños" or categoriaAux=="otros":
                        i=i+1
                        productos[auxCodigo] = {
                            "nombre": nombreAux,
                            "categoria": categoriaAux,
                            "talla": tallaAux,
                            "precio": precioAux,
                            "stock": stockAux
                        }
                    else: print("La categoria debe ser una de las especificadas")
                else:
                    print("El stock y precio deben ser mayor a 0")
            print("")
        except ValueError:
            print("ERROR: El precio debe ser un numero, el stock debe ser un numero entero")
def verProdcutos():
    print("==PRODUCTOS INGRESADOS==")
    print("1. Hombres")
    print("2. Mujeres")
    print("3. Niños")
    print("4. Otros")
    print("5. Todos")
    opcionAux=input("Ingrese la opcion: ")
    match opcionAux:
        case "1":
            for producto in productos:
                if(producto["categoria"]=="hombre"):
                    print(producto["nombre"])
                    print(producto["categoria"])


while True:
    print("==MENU==")
    print("1. Ingreso")
    print("2. Ver productos")
    print("3. Buscar producto")
    print("4. Salir")
    opcion=input("Ingrese una opcion: ")
    match opcion:
        case "1":
            Ingreso()
        case "4":
            print("Saliendo...")
            break
        case _:
            print("Opcion no valida")
