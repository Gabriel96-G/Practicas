###Funcion para crear el restaurante###

def crear_restaurante():
    nombre = input("===Ingrese nombre del restaurante===")
    print(f"El restaurante {nombre} fue creado con exito")
    return nombre

def mostrar_platillos(platillos):
    print("\n===PLATILLOS DISPONIBLES ===")
    for numero, datos in platillos.items ():
        print(numero, datos ["nombre"], "precio:", datos ["precio"], "stock:", datos ["stock"]),

def crear_orden(platillos, ordenes):
    print("\n===Crear una orden ===")
    orden = []
        
def menu_principal(nombre_restaurante, platillos, ordenes):
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ver platillos")
        print("2. Crear nueva orden")
        print("3. Ver órdenes")
        print("4. Cambiar estado de una orden")
        print("5. Finalizar una orden")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_platillos(platillos)
        elif opcion == "2":
            crear_orden(platillos, ordenes)
        elif opcion == "3":
            ver_ordenes(ordenes)
        elif opcion == "4":
            cambiar_estado(ordenes)
        elif opcion == "5":
            finalizar_orden(ordenes)
        elif opcion == "6":
            print("Gracias por usar el sistema, Adios", nombre_restaurante)
            break
        else:
            print("Opción no válida. Intente de nuevo.")


print("=== Bienvenido al Sistema de Restaurante ===")

nombre_restaurante = crear_restaurante()


platillos = {
    1: {"nombre": "Hamburguesa", "precio": 3500, "stock": 5},
    2: {"nombre": "Pizza", "precio": 4000, "stock": 4},
    3: {"nombre": "Refresco", "precio": 1200, "stock": 10}
}

ordenes = []

menu_principal(nombre_restaurante, platillos, ordenes)


