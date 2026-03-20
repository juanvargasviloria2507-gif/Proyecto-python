# Lista global donde se guardan los productos
productos = []

#Esta funcion se encarga de pedir y verificar el nombre del producto
def pedir_nombre():
    nombre_valido = False
    while not nombre_valido:
        nombre = input("\nIngrese el nombre del producto: ").strip()
        if nombre.replace(" ", "").isalpha():
            nombre_valido = True
        else:
            print("Solo se permiten letras")
    return nombre

#Esta funcion se encarga de pedir y verificar el precio del producto
def pedir_precio():
    precio = 0 
    while not (precio > 0):
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio <= 0:
                print("El precio debe ser mayor que 0")
        except ValueError:
            print("Por favor ingresar valores numéricos")
    return precio

#Esta funcion se encarga de pedir y verificar la cantidad del producto
def pedir_cantidad():
    cantidad = 0
    while not (cantidad > 0):
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))    
            if cantidad <= 0:
                print("La cantidad debe ser mayor que 0")
        except ValueError:
            print("Por favor ingresar valores numéricos")
        
    return cantidad            

#Esta funcion se encarga de calcular el total del producto
def calcular_total(precio, cantidad):
    return round(precio * cantidad, 1)

#Esta funcion se encarga de agregar productos
def agregar_productos():
    nombre = pedir_nombre()
    precio = pedir_precio()
    cantidad = pedir_cantidad()
    total = calcular_total(precio, cantidad)

    # Crea el diccionario del producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "total": total
    }

    #Esta funcion agrega a la lista
    productos.append(producto)
    
    print("\n----------------------------------")
    print("✅ Producto agregado correctamente")
    print("----------------------------------\n")
    print(producto)
    


def mostrar_inventario():
    print("\n----------------------------------")
    print("📦 Lista de productos:")
    print("----------------------------------\n")
    
    if not productos:
        print("\n No hay productos registrados")
        print("----------------------------------")
        input("Presione cualquier tecla para voler al menú")
        print("----------------------------------\n")
        return

    for i, p in enumerate(productos, 1):
        print(f"{i}. {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']} | Total: {p['total']}")
    input("Presione cualquier tecla para voler al menú")
        

def calcular_estadisticas():
    if not productos:
        print("\nNo hay productos registrados")
        return
    total_productos_agg = len(productos)
    total_items = sum(p["cantidad"] for p in productos)
    total_valor = sum(p["total"] for p in productos)

    print("\n📊 Estadisticas:")
    print("Total de productos agregados:", total_productos_agg)
    print("Total de unidades en inventario:", total_items)
    print("Valor total del inventario:", round(total_valor, 2))
    input("\nPresione cualquier tecla para voler al menú")

def agregar_producto():
    agregar_productos()
    agg = "s"
    while agg == "s" or agg == "S":
        agg = input("Desea agregar otro producto? (s/n)")
        if agg == "s" or agg == "S":
            agregar_productos()

    

    