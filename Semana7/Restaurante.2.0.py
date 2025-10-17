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
    orden = {"platillos": [] , "estado": "iniciado"}
    while True:
        mostrar_platillos(platillos)
        eleccion = int(input("Ingrese el numero del platillo que desea agregar (0 para terminar): "))
        if eleccion == 0:
            break
        
        if eleccion in platillos and platillos[eleccion]["stock"] > 0:
            orden["platillos"].append(eleccion)
            platillos[eleccion]["stock"] -= 1
            print("Platillo agregado:", platillos[eleccion]["nombre"])
        else:
            print("Opción no válida o platillo agotado.")
    if len(orden["platillos"]) > 0:
        ordenes.append(orden)
        print("Orden creada con éxito.")
    else:
        print("No se agregaron platillos a la orden.")

def ver_ordenes(ordenes):
    print("\n===Órdenes actuales===")

    if len(ordenes) == 0:
        print("No hay órdenes.")
    else: 
        for i, orden in enumerate(ordenes):
            print(f"Orden {i+1}: Estado: {orden['estado']}, Platillos: {orden['platillos']}")


def cambiar_estado(ordenes):
    print("\n===Cambiar estado de una orden===")
    if len(ordenes) == 0:
        print("No hay órdenes para cambiar estado.")
    else:
        for i, O in enumerate(ordenes):
            print(f"{i+1}. Estado: {O['estado']}, Platillos: {O['platillos']}")
        eleccion = int(input("Seleccione el número de la orden para cambiar estado: "))
        if eleccion >= 1 and eleccion <= len(ordenes):
            nuevo_estado = input("Ingrese el nuevo estado (iniciado, en preparacion, finalizado): ")
            ordenes[eleccion - 1] ["estado"] = nuevo_estado
            print("Estado actualizado.")
        else:
            print("Número de orden no válido.") 



def finalizar_orden(ordenes):
    print("\n===Finalizar una orden===")
    if len(ordenes) == 0:
        print("No hay órdenes registradas.")
    else:
        for i, O in enumerate(ordenes):
            print(f"{i+1}. Estado: {O['estado']}, Platillos: {O['platillos']}")
        eleccion = int(input("Seleccione el número de la orden para finalizar: "))
        if eleccion >= 0 and eleccion <= len(ordenes):
            orden = ordenes[eleccion-1]
            total = 0
            for p in orden["platillos"]:
                total += platillos[p]["precio"]
                print(f"El total de la orden es: {total}")
                print("Orden finalizada y eliminada del sistema.")
                ordenes.pop(eleccion-1)
        else:
            print("Número de orden inválido.")



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
 

