"""
Mini-Sistema de Venta de Celulares (CLI)
Curso: Principios de Programación (SOFT-01)
Tarea 2 - Lista de diccionarios, condicionales y ciclo while
"""

import random

# ---------------------------
# Variables globales
# ---------------------------

ARCHIVO = "celulares.txt"   # Nombre del archivo de texto
productos = []              # Lista de diccionarios
modificado = False          # Variable global booleana para saber si hubo cambios


# ---------------------------
# Funciones de apoyo (utilitarias)
# ---------------------------

def generar_id_unico():
    """Genera un ID aleatorio entre 1 y 5000 que no esté repetido en la lista."""
    existentes = {cel["id"] for cel in productos}
    while True:
        nuevo_id = random.randint(1, 5000)
        if nuevo_id not in existentes:
            return nuevo_id


def mostrar_celular(cel):
    """Muestra en pantalla la información de un celular."""
    print(
        f"ID: {cel['id']} | "
        f"Marca: {cel['marca']} | "
        f"Modelo: {cel['modelo']} | "
        f"Precio: ₡{cel['precio']:.2f} | "
        f"Stock: {cel['stock']}"
    )


def listar_celulares():
    """Lista todos los celulares que están en memoria."""
    if not productos:
        print("No hay celulares cargados.")
        return
    print("\n=== LISTA DE CELULARES ===")
    for cel in productos:
        mostrar_celular(cel)


def pedir_entero_positivo(mensaje, permitir_cero=False):
    """Pide un entero positivo (y opcionalmente permite 0)."""
    while True:
        dato = input(mensaje)
        try:
            valor = int(dato)
            if valor < 0 or (not permitir_cero and valor == 0):
                print("Debe ingresar un número entero positivo.")
            else:
                return valor
        except ValueError:
            print("Debe ingresar un número entero válido.")


def pedir_float_positivo(mensaje):
    """Pide un número real mayor que cero."""
    while True:
        dato = input(mensaje)
        try:
            valor = float(dato)
            if valor <= 0:
                print("Debe ingresar un número mayor que cero.")
            else:
                return valor
        except ValueError:
            print("Debe ingresar un número válido (use punto decimal si es necesario).")


def existe_marca_modelo(marca, modelo):
    """Devuelve True si ya existe un celular con la misma marca y modelo (no se permiten)."""
    for cel in productos:
        if cel["marca"].lower() == marca.lower() and cel["modelo"].lower() == modelo.lower():
            return True
    return False


def buscar_por_id(id_buscar):
    """Busca un celular por ID. Devuelve el diccionario o None."""
    for cel in productos:
        if cel["id"] == id_buscar:
            return cel
    return None


def buscar_por_marca(marca):
    """Devuelve una lista de celulares que coinciden con la marca dada."""
    return [cel for cel in productos if cel["marca"].lower() == marca.lower()]


# ---------------------------
# Funciones de opciones del menú
# ---------------------------

def cargar_informacion():
    """
    Cargar información: lee el archivo de texto,
    almacena los datos en la lista de diccionarios y los muestra.
    """
    global productos, modificado
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            productos = []
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split(",")
                # Formato previsto: id,marca,modelo,precio,stock
                if len(partes) != 5:
                    print(f"Línea ignorada por formato inválido: {linea}")
                    continue
                try:
                    id_cel = int(partes[0])
                    marca = partes[1]
                    modelo = partes[2]
                    precio = float(partes[3])
                    stock = int(partes[4])
                except ValueError:
                    print(f"Línea ignorada por tipos inválidos: {linea}")
                    continue

                cel = {
                    "id": id_cel,
                    "marca": marca,
                    "modelo": modelo,
                    "precio": precio,
                    "stock": stock
                }
                productos.append(cel)

        modificado = False
        print("Información cargada correctamente desde el archivo.")
        listar_celulares()

    except FileNotFoundError:
        print("No se encontró el archivo. Se creará automáticamente al guardar.")
        productos = []
        modificado = False


def guardar_informacion():
    """
    Guardar información: vuelca todo el contenido de la lista de diccionarios
    en el archivo de texto.
    """
    global modificado
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        for cel in productos:
            linea = f"{cel['id']},{cel['marca']},{cel['modelo']},{cel['precio']},{cel['stock']}\n"
            f.write(linea)
    modificado = False
    print("Información guardada correctamente en el archivo.")


def agregar_stock():
    """
    Agregar stock: pide marca, modelo, precio y unidades.
    Genera un ID aleatorio y almacena el celular en la lista.
    No permite marca+modelo repetidos, precios negativos ni cantidades negativas.
    """
    global modificado
    print("\n=== AGREGAR CELULAR / STOCK ===")
    marca = input("Ingrese la marca del celular: ").strip()
    modelo = input("Ingrese el modelo del celular: ").strip()

    if not marca or not modelo:
        print("La marca y el modelo no pueden estar vacíos.")
        return

    # No se pueden aceptar celulares con mismo modelo Y marca
    if existe_marca_modelo(marca, modelo):
        print("Ya existe un celular con esa marca y modelo.")
        print("Use la opción 'Cambiar stock' si desea modificar las unidades.")
        return

    precio = pedir_float_positivo("Ingrese el precio del celular: ")
    cantidad = pedir_entero_positivo("Ingrese la cantidad de unidades adquiridas: ")

    nuevo_id = generar_id_unico()
    cel = {
        "id": nuevo_id,
        "marca": marca,
        "modelo": modelo,
        "precio": precio,
        "stock": cantidad
    }
    productos.append(cel)
    modificado = True

    print("Celular agregado correctamente:")
    mostrar_celular(cel)


def cambiar_precio():
    """
    Cambiar precio: pide la marca y, si hay varios modelos,
    permite elegir uno por ID. Actualiza el precio.
    """
    global modificado
    print("\n=== CAMBIAR PRECIO ===")
    marca = input("Ingrese la marca del celular: ").strip()
    if not marca:
        print("La marca no puede estar vacía.")
        return

    encontrados = buscar_por_marca(marca)

    if not encontrados:
        print("No se encontraron celulares con esa marca.")
        return

    if len(encontrados) == 1:
        cel = encontrados[0]
    else:
        print("Se encontraron varios modelos para esa marca:")
        for cel_tmp in encontrados:
            mostrar_celular(cel_tmp)
        id_cel = pedir_entero_positivo("Ingrese el ID del celular al que desea cambiarle el precio: ")
        cel = buscar_por_id(id_cel)
        if (cel is None) or (cel not in encontrados):
            print("ID no válido para esa marca.")
            return

    print("Celular seleccionado:")
    mostrar_celular(cel)
    nuevo_precio = pedir_float_positivo("Ingrese el nuevo precio: ")
    cel["precio"] = nuevo_precio
    modificado = True

    print("Precio actualizado correctamente:")
    mostrar_celular(cel)


def cambiar_stock():
    """
    Cambiar stock: pide el ID del celular y modifica su stock.
    Permite dejar el stock en 0, pero no valores negativos.
    """
    global modificado
    print("\n=== CAMBIAR STOCK ===")
    if not productos:
        print("No hay celulares en el sistema.")
        return

    listar_celulares()
    id_cel = pedir_entero_positivo("Ingrese el ID del celular al que desea cambiarle el stock: ")
    cel = buscar_por_id(id_cel)
    if cel is None:
        print("No se encontró un celular con ese ID.")
        return

    print("Celular seleccionado:")
    mostrar_celular(cel)
    nuevo_stock = pedir_entero_positivo("Ingrese el nuevo stock (puede ser 0): ", permitir_cero=True)
    cel["stock"] = nuevo_stock
    modificado = True

    print("Stock actualizado correctamente:")
    mostrar_celular(cel)


def opcion_buscar_celular_por_marca():
    """
    Buscar celular por marca: lista todos los celulares
    que coinciden con una marca indicada.
    """
    print("\n=== BUSCAR CELULAR POR MARCA ===")
    marca = input("Ingrese la marca a buscar: ").strip()
    if not marca:
        print("La marca no puede estar vacía.")
        return

    encontrados = buscar_por_marca(marca)
    if not encontrados:
        print("No se encontraron celulares para esa marca.")
    else:
        print(f"Se encontraron {len(encontrados)} celular(es) de la marca {marca}:")
        for cel in encontrados:
            mostrar_celular(cel)


def vender():
    """
    Vender: a partir de marca y modelo,
    permite vender una cantidad de unidades.
    Valida:
      - que exista el celular;
      - que el stock sea suficiente;
      - que la cantidad no sea negativa.
    """
    global modificado
    print("\n=== VENDER CELULAR ===")
    marca = input("Ingrese la marca del celular: ").strip()
    modelo = input("Ingrese el modelo del celular: ").strip()

    if not marca or not modelo:
        print("La marca y el modelo no pueden estar vacíos.")
        return

    seleccionado = None
    for cel in productos:
        if cel["marca"].lower() == marca.lower() and cel["modelo"].lower() == modelo.lower():
            seleccionado = cel
            break

    if seleccionado is None:
        print("No se encontró un celular con esa marca y modelo.")
        return

    print("Celular seleccionado:")
    mostrar_celular(seleccionado)

    if seleccionado["stock"] <= 0:
        print("No hay stock disponible para este celular.")
        return

    cantidad = pedir_entero_positivo("Ingrese la cantidad a vender: ")
    if cantidad > seleccionado["stock"]:
        print("No se puede vender más unidades que las disponibles en stock.")
        return

    seleccionado["stock"] -= cantidad
    total = cantidad * seleccionado["precio"]
    modificado = True

    print(f"Venta realizada correctamente. Total a pagar: ₡{total:.2f}")
    print("Stock restante:")
    mostrar_celular(seleccionado)


# ---------------------------
# Menú principal
# ---------------------------

def mostrar_menu():
    """Muestra el menú principal del sistema."""
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Cargar información desde archivo")
    print("2. Agregar stock (nuevo celular)")
    print("3. Cambiar precio")
    print("4. Cambiar stock")
    print("5. Buscar celular por marca")
    print("6. Vender")
    print("7. Listar celulares")
    print("8. Guardar información en archivo")
    print("9. Salir")


def main():
    """Controla el flujo principal usando un ciclo while."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cargar_informacion()
        elif opcion == "2":
            agregar_stock()
        elif opcion == "3":
            cambiar_precio()
        elif opcion == "4":
            cambiar_stock()
        elif opcion == "5":
            opcion_buscar_celular_por_marca()
        elif opcion == "6":
            vender()
        elif opcion == "7":
            listar_celulares()
        elif opcion == "8":
            guardar_informacion()
        elif opcion == "9":
            # Opción salir: guarda SÓLO si hubo modificaciones
            if modificado:
                print("Se detectaron cambios. Guardando información antes de salir...")
                guardar_informacion()
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
