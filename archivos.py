
import csv
import os


def guardar_csv(inventario, ruta):
    if not inventario:
        print("⚠️ Inventario vacío, no se puede guardar")
        return

    try:
        ruta = os.path.normpath(ruta)
        carpeta = os.path.dirname(ruta)
        if carpeta != "":
            os.makedirs(carpeta, exist_ok=True)

        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)

            writer.writerow(["nombre", "precio", "cantidad"])

            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print(f"✅ Archivo guardado en: {ruta}")

    except Exception as e:
        print("❌ Error al guardar:", e)


def cargar_csv(ruta):
    inventario = []
    errores = 0

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)

            encabezado = next(reader)
            if encabezado != ["nombre", "precio", "cantidad"]:
                print("❌ Encabezado inválido")
                return []

            for fila in reader:
                if len(fila) != 3:
                    errores += 1
                    continue

                try:
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    if precio < 0 or cantidad < 0:
                        errores += 1
                        continue

                    # 🔥 AQUÍ ESTÁ EL FIX (agregar total)
                    producto = {
                        "nombre": fila[0],
                        "precio": precio,
                        "cantidad": cantidad,
                        "total": round(precio * cantidad, 1)
                    }

                    inventario.append(producto)

                except:
                    errores += 1

        print(f"✅ Productos cargados: {len(inventario)}")
        print(f"⚠️ Filas inválidas omitidas: {errores}")
        print("✅ Archivo cargado correctamente")

        return inventario

    except FileNotFoundError:
        print("❌ Archivo no encontrado")
        return []