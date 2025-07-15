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
                categoriaAux=input("Ingrese el categoria del producto: (Hombre, Mujer, Niño, etc)")
                tallaAux=input("Ingrese el talla del producto: ")
                precioAux=float(input("Ingrese el precio del producto: "))
                stockAux=int(input("Ingrese el stock del producto: "))
                if stockAux>0 and precioAux>0:
                    i=i+1
                    productos[auxCodigo] = {
                        "nombre": nombreAux,
                        "categoria": categoriaAux,
                        "talla": tallaAux,
                        "precio": precioAux,
                        "stock": stockAux
                    }
            print("")
        except ValueError:
            print("ERROR: El precio debe ser un numero, el stock debe ser un numero entero")
