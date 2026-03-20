import time
import inventario

# Este bloque de codigo se encarga de mostrar el menu principal
def menu():
    print("\n----------------------------------")
    print("bienvenido al menu del inventario")
    print("----------------------------------\n")
    print("1. Agregar productos.")
    print("2. Mostrar inventario.")
    print("3. Calcular estadisticas.")
    print("4. Salir.")

# Este bloque de codigo se encarga de ejecutar las funciones del programa    
def main():
    
    opcion = 0
    while opcion != 4:
            menu()
            opcion =  int (input("\nIngrese una opcion a realizar en el menu: ") )
            if opcion == 1:
                inventario.agregar_producto()
            elif opcion == 2:
                inventario.mostrar_inventario()
            elif opcion == 3:
                inventario.calcular_estadisticas()
            elif opcion > 4 or opcion < 1:
                 print("----------------------------------")
                 print("Opcion no valida, Intentelo de nuevo")
                 print("----------------------------------")
                 time.sleep(2)  # pausa de 2 segundos
            

        # MAIN
if __name__ == "__main__":
     main()        
