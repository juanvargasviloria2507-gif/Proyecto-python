
#Este bloque de codigo valida y pide nombre del producto.
while True:
        nombre = input ("ingrese el nombre del producto: ").strip()
        if nombre.replace(" ", "").isalpha(): #Esta linea de codigo permite validar que solo haya letras y espacios
                print("Nombre ingresado correctamente:", nombre)
                break
        else:
            print("solo se permiten letras")
#Este bloque de codigo valida y pide precio
while True:
        try:
            precio = float(input("ingrese el precio del producto: "))
            if precio > 0:
                print("precio ingresado correctamente:", precio)
                break
            else:
                print("el precio debe ser mayor que 0")
        except ValueError:
            print("por favor ingresar valores numericos")
#Este bloque de codigo valida y pide cantidad
while True:
        try:
              
            cantidad = int(input("ingrese la cantidad del producto: "))
            if cantidad > 0:
                print("Cantidad ingresada correctamente:", cantidad)
                break
            else:
                print("La cantidad ingresada debe ser que 0")
        except ValueError:
             print("Por favor ingresar valores numericos")


print("\nNombre:", nombre, "Precio:", precio, "Cantidad:", cantidad)

      

nombre = ()
precio = ()
cantidad = ()
costo_total = (precio * cantidad)
