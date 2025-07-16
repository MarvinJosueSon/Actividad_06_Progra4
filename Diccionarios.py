from ipaddress import summarize_address_range

productos = {}
def Ingreso():
    cantidad=int(input("Ingrese cuantos productos quiere agregar: "))
    i=1
    while i <= cantidad:
        try:
            print(f"Ingreso producto #{i}")
            auxCodigo = input("Ingrese el codigo del producto: ")
            if auxCodigo in productos:
                print("ERROR: El codigo del producto ya existe")
            else:
                nombreAux=input("Ingrese el nombre del producto: ")

                precioAux=float(input("Ingrese el precio del producto: "))
                stockAux=int(input("Ingrese el stock del producto: "))
                if stockAux>0 and precioAux>0:
                    categoriaAux = input("Ingrese el categoria del producto: (hombre, mujer, niños, otros): ").lower()

                    if categoriaAux == "mujer" or categoriaAux == "hombre" or categoriaAux == "niños" or categoriaAux=="otros":
                        tallaAux = input("Ingrese el talla del producto: ")
                        i=i+1
                        productos[auxCodigo] = {
                            "nombre": nombreAux,
                            "categoria": categoriaAux,
                            "talla": tallaAux,
                            "precio": precioAux,
                            "stock": stockAux
                        }
                    else: print("ERROR: La categoria debe ser una de las especificadas")
                else:
                    print("ERROR: El stock y precio deben ser mayor a 0")
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
            contadorHombres=0
            print("== CATEGORÍA: HOMBRES ==")
            for clave, producto in productos.items():
                if producto["categoria"] == "hombre":
                    print(f"Código: {clave}")
                    print(f"Nombre: {producto['nombre']}")
                    print(f"Talla: {producto['talla']}")
                    print(f"Precio: {producto['precio']}")
                    print(f"Stock: {producto['stock']}")
                    suma = suma + (producto["precio"] * producto["stock"])
                    contadorHombres=contadorHombres + 1
                    print("----------")
            if contadorHombres>0:
                print(f"Valor total de inventario: Q{suma}")
                print(f"Cantidad: {contadorHombres}")
            else:
                print("No se ha encontrado ningun producto en esta categoria")
        case "2":
            suma=0
            contadorMujeres=0
            print("== CATEGORÍA: MUJERES ==")
            for clave, producto in productos.items():
                if producto["categoria"] == "mujer":
                    contadorMujeres = contadorMujeres + 1
                    print(f"Código: {clave}")
                    print(f"Nombre: {producto['nombre']}")
                    print(f"Talla: {producto['talla']}")
                    print(f"Precio: {producto['precio']}")
                    print(f"Stock: {producto['stock']}")
                    suma=suma + (producto["precio"] * producto["stock"])
                    print("----------")
            if contadorMujeres>0:
                print(f"Valor total de inventario: Q{suma}")
                print(f"Cantidad: {contadorMujeres}")
            else:
                print("No se ha encontrado ningun producto en esta categoria")

        case "3":
            suma=0
            contadorNiños=0
            print("== CATEGORÍA: NIÑOS ==")
            for clave, producto in productos.items():
                if producto["categoria"] == "niños":
                    contadorNiños=contadorNiños+1
                    print(f"Código: {clave}")
                    print(f"Nombre: {producto['nombre']}")
                    print(f"Talla: {producto['talla']}")
                    print(f"Precio: {producto['precio']}")
                    print(f"Stock: {producto['stock']}")
                    suma = suma + (producto["precio"] * producto["stock"])
                    print("----------")
            if contadorNiños>0:
                print(f"Valor total de inventario: Q{suma}")
                print(f"Cantidad: {contadorNiños}")
            else:
                print("No se ha encontrado ningun producto en esta categoria")
        case "4":
            suma=0
            contadorOtros=0
            print("== CATEGORÍA: OTROS ==")
            for clave, producto in productos.items():
                if producto["categoria"] == "otros":
                    contadorOtros=contadorOtros+1
                    print(f"Código: {clave}")
                    print(f"Nombre: {producto['nombre']}")
                    print(f"Talla: {producto['talla']}")
                    print(f"Precio: {producto['precio']}")
                    print(f"Stock: {producto['stock']}")
                    suma = suma + (producto["precio"] * producto["stock"])
                    print("----------")
            if contadorOtros>0:
                print(f"Valor total de inventario: Q{suma}")
                print(f"Cantidad: {contadorOtros}")
            else:
                print("No se ha encontrado ningun producto en esta categoria")
        case "5":
            suma=0
            contador=0
            print("== TODOS LOS PRODUCTOS ==")
            for clave, producto in productos.items():
                contador = contador + 1
                print(f"Código: {clave}")
                print(f"Nombre: {producto['nombre']}")
                print(f"Categoría: {producto['categoria']}")
                print(f"Talla: {producto['talla']}")
                print(f"Precio: {producto['precio']}")
                print(f"Stock: {producto['stock']}")
                suma = suma + (producto["precio"] * producto["stock"])
                print("----------")
            if contador>0:
                print(f"Valor total de inventario: Q{suma}")
                print(f"Cantidad: {contador}")
            else:
                print("No se ha encontrado ningun producto")
        case _:
            print("Opción no encontrada")

def buscarProductos():
    buscar=input("Ingrese el codigo del producto a buscar: ")
    if buscar in productos:
        print(f'categoría: {productos[buscar]["categoria"]}')
        print(f'nombre: {productos[buscar]["nombre"]}')
        print(f'talla: {productos[buscar]["talla"]}')
        print(f'precio: {productos[buscar]["precio"]}')
        print(f'stock: {productos[buscar]["stock"]}')
        print(f"Suma de precio: {productos[buscar]['precio']*productos[buscar]['stock']}")


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
            buscarProductos()
        case "4":
            print("Saliendo...")
            break
        case _:
            print("Opcion no valida")
