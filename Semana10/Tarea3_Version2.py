"""
Mini Sistema de Gestión de Tareas  (CLI)
- Usa una lista en memoria para manejar las tareas.
- Guarda y lee las tareas desde 'tareas.txt'.
- No usa librerías externas. 

"""


def cargar_tareas():
    print("\n=== Sistema de Gestion de Tareas ===")
    tareas = []
    try:
        with open("tareas.txt", "r") as archivo:
            for linea in archivo:
                tareas.append(linea.strip())
        if len(tareas) == 0:
            print("No hay tareas guardadas.")
        else:
            print("Lista de tareas cargadas:")
            for i, tarea in enumerate(tareas, start=1):
                print(f" {i}.  {tarea}")
            
    except FileNotFoundError:
        print("No se encontró el archivo de tareas. Se creará uno nuevo al guardar.")
    return tareas


def agregar_tarea(tareas):
    nueva_tarea = input("Ingrese nueva tarea: ")
    if nueva_tarea.strip() == "":
        print("No puede ingresar una tarea vacía.")
        return
    tareas.append(nueva_tarea)
    print("Tarea agregada correctamente.")
    


def eliminar_tarea(tareas):
    if len(tareas) == 0:
        print("No hay tareas para eliminar.")
        return tareas
    try:
        num = int(input("Ingrese el número de la tarea a eliminar: "))
        if 1 <= num <= len(tareas):
            eliminada = tareas.pop(num - 1)
            print(f"Tarea eliminada: {eliminada}")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Debe ingresar un número válido.")
    return tareas


def guardar_tareas(tareas):
    with open("tareas.txt", "w") as archivo:
        for tarea in tareas:
            archivo.write(tarea + "\n")
    print("Tareas guardadas en tareas.txt")


def menu():
    tareas = []
    while True:

        print("\n=== Menú de Gestión de Tareas ===")
        print("1. Cargar tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Guardar y salir")
        opcion = input("Seleccione una opción (1-4): ")
    
        if opcion == "1":
            tareas =cargar_tareas()
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            eliminar_tarea(tareas)
        elif opcion == "4":
            guardar_tareas(tareas)
            break
        else:
            print("Opción no válida. Intente nuevamente.")
menu()