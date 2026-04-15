def calcular_total(precio, cantidad):
    return round(precio * cantidad, 1)


def agregar_producto(inventario, nombre, precio, cantidad):
    total = calcular_total(precio, cantidad)

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "total": total
    }

    inventario.append(producto)
    return producto


def mostrar_inventario(inventario):
    print("\n----------------------------------")
    print("📦 Lista de productos:")
    print("----------------------------------\n")

    if not inventario:
        print("No hay productos registrados")
        return

    for i, p in enumerate(inventario, 1):
        print(f"{i}. {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']} | Total: {p['total']}")


def buscar_producto(inventario, nombre):
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    producto = buscar_producto(inventario, nombre)

    if producto:
        if nuevo_precio is not None:
            producto["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            producto["cantidad"] = nueva_cantidad

        producto["total"] = calcular_total(producto["precio"], producto["cantidad"])
        return producto

    return None


def eliminar_producto(inventario, nombre):
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            inventario.remove(p)
            return p
    return None


def calcular_estadisticas(inventario):
    if not inventario:
        return None

    total_productos = len(inventario)
    total_unidades = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["total"] for p in inventario)

    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "total_productos": total_productos,
        "total_unidades": total_unidades,
        "valor_total": round(valor_total, 2),
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }