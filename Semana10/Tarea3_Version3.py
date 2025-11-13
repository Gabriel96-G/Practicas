"""
Mini Sistema de Gestión de Tareas  (CLI)
- Usa una lista en memoria para manejar las tareas.
- Guarda y lee las tareas desde 'tareas.txt'.
- No usa librerías externas.
"""

NOMBRE_ARCHIVO = "tareas.txt"


def cargar_tareas():
    print("\n=== Sistema de Gestion de Tareas ===")
    tareas = []
    try:
        with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    tareas.append(linea)

        if len(tareas) == 0:
            print("No hay tareas guardadas.")
        else:
            print("Lista de tareas cargadas:")
            for i, tarea in enumerate(tareas, start=1):
                print(f"{i}. {tarea}")

    except FileNotFoundError:
        # Caso archivo no existe: mensaje como la consigna
        print("No se encontró el archivo, se creará uno nuevo...")
        with open(NOMBRE_ARCHIVO, "w", encoding="utf-8"):
            pass
        print(f"Archivo creado: {NOMBRE_ARCHIVO}")

    return tareas


def agregar_tarea(tareas):
    nueva_tarea = input("Ingrese nueva tarea: ").strip()
    if nueva_tarea == "":
        print("No puede ingresar una tarea vacía.")
        return

    tareas.append(nueva_tarea)
    print("Tarea agregada correctamente.")

    # La consigna dice: agregar a la lista Y al archivo
    try:
        with open(NOMBRE_ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(nueva_tarea + "\n")
    except FileNotFoundError:
        # Si por algo no existe aún, lo creamos y escribimos
        with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as archivo:
            archivo.write(nueva_tarea + "\n")


def eliminar_tarea(tareas):
    if len(tareas) == 0:
        print("No hay tareas para eliminar.")
        return

    print("Tareas actuales:")
    for i, tarea in enumerate(tareas, start=1):
        print(f"{i}. {tarea}")

    try:
        indice = int(input("Ingrese el número de la tarea a eliminar: "))
        if 1 <= indice <= len(tareas):
            tarea_eliminada = tareas.pop(indice - 1)
            print(f"Tarea '{tarea_eliminada}' eliminada correctamente.")

            # Actualizar archivo con la lista resultante
            with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as archivo:
                for tarea in tareas:
                    archivo.write(tarea + "\n")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada inválida. Por favor ingrese un número válido.")


def guardar_tareas(tareas):
    with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as archivo:
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
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            tareas = cargar_tareas()
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
