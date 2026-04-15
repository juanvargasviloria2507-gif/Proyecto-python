from servicios import *
from archivos import *


def pedir_nombre():
    valido = False
    while not valido:
        nombre = input("Ingrese el nombre: ").strip()
        if nombre.replace(" ", "").isalpha():
            valido = True
        else:
            print("Solo letras")
    return nombre


def pedir_precio():
    valido = False
    while not valido:
        try:
            precio = float(input("Ingrese precio: "))
            if precio > 0:
                valido = True
            else:
                print("Debe ser mayor a 0")
        except:
            print("Precio inválido")
    return precio


def pedir_cantidad():
    valido = False
    while not valido:
        try:
            cantidad = int(input("Ingrese cantidad: "))
            if cantidad > 0:
                valido = True
            else:
                print("Debe ser mayor a 0")
        except:
            print("Cantidad inválida")
    return cantidad


def main():
    print("Ruta actual:", os.getcwd())
    inventario = []
    opcion = ""

    while opcion != "9":
        print("\n====== INVENTARIO ======")
        print("1. Agregar")
        print("2. Mostrar")
        print("3. Buscar")
        print("4. Actualizar")
        print("5. Eliminar")
        print("6. Estadísticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            nombre = pedir_nombre()
            precio = pedir_precio()
            cantidad = pedir_cantidad()

            producto = agregar_producto(inventario, nombre, precio, cantidad)
            print("✅ Agregado:", producto)

        elif opcion == "2":
            mostrar_inventario(inventario)

        elif opcion == "3":
            nombre = input("Buscar: ")
            p = buscar_producto(inventario, nombre)
            print(p if p else "❌ No encontrado")

        elif opcion == "4":
            mostrar_inventario(inventario)
            nombre = input("Producto a actualizar: ")

            precio = pedir_precio()
            cantidad = pedir_cantidad()

            actualizado = actualizar_producto(inventario, nombre, precio, cantidad)
            print("✅ Actualizado:", actualizado) if actualizado else print("❌ No encontrado")

        elif opcion == "5":
            mostrar_inventario(inventario)
            nombre = input("Producto a eliminar: ")

            eliminado = eliminar_producto(inventario, nombre)
            print("🗑️ Eliminado:", eliminado) if eliminado else print("❌ No encontrado")

        elif opcion == "6":
            stats = calcular_estadisticas(inventario)
            print(stats if stats else "Inventario vacío")

        elif opcion == "7":
            ruta = input("Ruta: ")
            guardar_csv(inventario, ruta)

        elif opcion == "8":
            ruta = input("Ruta: ")
            datos = cargar_csv(ruta)

            decision = input("¿Sobrescribir inventario? (S/N): ")

            if decision.lower() == "s":
                inventario = datos
            else:
                for nuevo in datos:
                    existente = buscar_producto(inventario, nuevo["nombre"])
                    if existente:
                        existente["cantidad"] += nuevo["cantidad"]
                        existente["precio"] = nuevo["precio"]
                        existente["total"] = round(
                            existente["precio"] * existente["cantidad"], 1
                        )
                    else:
                        inventario.append(nuevo)

        elif opcion == "9":
            print("👋 Saliendo...")

        else:
            print("❌ Opción inválida")


if __name__ == "__main__":
    main()