productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
    '8475HD': [387990,10], 
    '2175HD': [327990,4], 
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], 
    '123FHD': [290890,32], 
    '342FHD': [444990,7],
    'GF75HD': [749990,2], 
    'UWU131HD': [349990,1], 
}

def stock_marca (marca):
    total = 0
    for modelo in productos:
         if productos[modelo][0] == marca or productos[modelo][0] == marca.upper() or productos[modelo][0] == marca.capitalize():
            total += stock[modelo][1]
    print("El stock es:", total)

def busqueda_precio (p_min, p_max ):
    try:
        p_min = int(p_min)
    except:
        print("Debe ingresar valores enteros!!")
        return
    try:
        p_max = int(p_max)
    except:
        print("Debe ingresar valores enteros!!")
        return

    disponibles = []
    for modelo in stock:
        precio = stock[modelo][0]
        unidades = stock[modelo][1]
        if p_min <= precio <= p_max and unidades > 0:
            marca = productos[modelo][0]
            disponibles.append(marca + "--" + modelo)

    if disponibles == []:
        print("No hay telefonos en ese rango de precios.")
    else:
        disponibles.sort()
        print("Telefonos disponibles:", disponibles)

def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p
        return True
    else:
        return False
    
def menu():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1. Stock por marca")
        print("2. Buscar por rango de precios")
        print("3. Actualizar precio de modelo")
        print("4. Salir")
        try:
            opcion = int(input("Ingrese opcion: "))
        except:
            print("Debe seleccionar una opcion valida!!")
            continue

        if opcion == 1:
            marca = input("Ingrese marca a consultar: ")
            stock_marca(marca)

        elif opcion == 2:
            p_min = input("Ingrese precio minimo: ")
            p_max = input("Ingrese precio maximo: ")
            busqueda_precio(p_min, p_max)

        elif opcion == 3:
            while True:
                modelo = input("Ingrese modelo a actualizar: ")
                try:
                    p = int(input("Ingrese precio nuevo: "))
                    actualizado = actualizar_precio(modelo, p)
                    if actualizado:
                        print("Precio actualizado!!")
                    else:
                        print("El modelo no existe!!")
                except:
                    print("Debe ingresar un precio valido!!")
                continuar = input("¿Desea actualizar otro precio (s/n)?: ")
                if continuar != "s":
                    break

        elif opcion == 4:
            print("Programa finalizado.")
            break

        else:
            print("Debe seleccionar una opcion valida!!")

menu()