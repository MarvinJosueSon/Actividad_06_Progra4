from ipaddress import summarize_address_range

productos = {}
def Ingreso():
    cantidad=int(input("Ingrese cuantos productos quiere agregar: "))
    i=1
    while i <= cantidad:
        try:
            auxCodigo = input("Ingrese el codigo del producto: ")
            if auxCodigo in productos:
                print("El codigo del producto ya existe")
            else:
                nombreAux=input("Ingrese el nombre del producto: ")
                categoriaAux=input("Ingrese el categoria del producto: (hombre, mujer, niños, otros: )").lower()
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
def verProductos():
    print("== PRODUCTOS INGRESADOS ==")
    print("1. Hombres")
    print("2. Mujeres")
    print("3. Niños")
    print("4. Otros")
    print("5. Todos")
    opcionAux = input("Ingrese la opción: ")

    match opcionAux:
        case "1":
            suma=0
            print("== CATEGORÍA: HOMBRES ==")
            for clave, producto in productos.items():
                if producto["categoria"] == "hombre":
                    print(f"Código: {clave}")
                    print(f"Nombre: {producto['nombre']}")
                    print(f"Talla: {producto['talla']}")
                    print(f"Precio: {producto['precio']}")
                    print(f"Stock: {producto['stock']}")
                    suma = suma + (producto["precio"] * producto["stock"])
                    print(f"Valor total de inventario: {suma}")
                    print("----------")


        case "2":
            suma=0
            print("== CATEGORÍA: MUJERES ==")
            for clave, producto in productos.items():
                if producto["categoria"] == "mujer":
                    print(f"Código: {clave}")
                    print(f"Nombre: {producto['nombre']}")
                    print(f"Talla: {producto['talla']}")
                    print(f"Precio: {producto['precio']}")
                    print(f"Stock: {producto['stock']}")
                    suma = suma + (producto["precio"] * producto["stock"])
                    print(f"Valor total de inventario: {suma}")
                    print("----------")

        case "3":
            suma=0
            print("== CATEGORÍA: NIÑOS ==")
            for clave, producto in productos.items():
                if producto["categoria"] == "niños":
                    print(f"Código: {clave}")
                    print(f"Nombre: {producto['nombre']}")
                    print(f"Talla: {producto['talla']}")
                    print(f"Precio: {producto['precio']}")
                    print(f"Stock: {producto['stock']}")
                    suma = suma + (producto["precio"] * producto["stock"])
                    print(f"Valor total de inventario: {suma}")
                    print("----------")

        case "4":
            suma=0
            print("== CATEGORÍA: OTROS ==")
            for clave, producto in productos.items():
                if producto["categoria"] == "otros":
                    print(f"Código: {clave}")
                    print(f"Nombre: {producto['nombre']}")
                    print(f"Talla: {producto['talla']}")
                    print(f"Precio: {producto['precio']}")
                    print(f"Stock: {producto['stock']}")
                    suma = suma + (producto["precio"] * producto["stock"])
                    print(f"Valor total de inventario: {suma}")
                    print("----------")

        case "5":
            suma=0
            print("== TODOS LOS PRODUCTOS ==")
            for clave, producto in productos.items():
                print(f"Código: {clave}")
                print(f"Nombre: {producto['nombre']}")
                print(f"Categoría: {producto['categoria']}")
                print(f"Talla: {producto['talla']}")
                print(f"Precio: {producto['precio']}")
                print(f"Stock: {producto['stock']}")
                suma = suma + (producto["precio"] * producto["stock"])
                print(f"Valor total de inventario: {suma}")
                print("----------")

        case _:
            print("Opción no encontrada")

def buscarProductos():


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
        case "2":
            verProductos()
        case "3":

        case "4":
            print("Saliendo...")
            break
        case _:
            print("Opcion no valida")
