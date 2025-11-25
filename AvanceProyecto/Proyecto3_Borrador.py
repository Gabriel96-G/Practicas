import random
import time
import os

# Constantes
ancho = 10
alto = 20
ticket_inicial = 0.5
archivo_puntajes = "scores.txt"

# Piezas
I = [(-2,0),(-1,0),(0,0),(1,0)]
O = [(0,0),(1,0),(0,1),(1,1)]
T = [(-1,0),(0,0),(1,0),(0,1)]
L = [(-1,0),(0,0),(1,0),(1,1)]
J = [(-1,0),(0,0),(1,0),(-1,1)]
S = [(0,0),(1,0),(-1,1),(0,1)]
Z = [(-1,0),(0,0),(0,1),(1,1)]

PIEZAS = [I, O, T, L, J, S, Z]
NOMBRES_PIEZAS = ['I', 'O', 'T', 'L', 'J', 'S', 'Z']

# Utilidades
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def crear_tablero():
    tablero = []
    for _ in range(alto):
        tablero.append([0] * ancho)
    return tablero

def copiar_lista(l):
    return [list(row) for row in l]

# Dibujar tablero
def imprimir_tablero(tablero, pieza=None, px=0, py=0, puntuacion=0):
    copia = copiar_lista(tablero)
    if pieza:
        for (x, y) in pieza:
            tx = px + x
            ty = py + y
            if 0 <= ty < alto and 0 <= tx < ancho:
                copia[ty][tx] = 1

    limpiar_pantalla()
    print("Puntaje:", puntuacion)
    print("=" * (ancho + 4))

    for fila in copia:
        linea = "<!" + "".join("#" if c else " " for c in fila) + "!>"
        print(linea)
    print("=" * (ancho + 4))
    print("Controles: a=izquierda, d=derecha, s=abajo, w=rotar, [enter]=nada")

# Colisiones
def colision_pieza(tablero, pieza, px, py):
    for (x, y) in pieza:
        tx = px + x
        ty = py + y

        if tx < 0 or tx >= ancho or ty >= alto:
            return True

        if ty >= 0 and tablero[ty][tx] == 1:
            return True

    return False

# Pegar pieza al tablero
def agregar_pieza_tablero(tablero, pieza, px, py):
    for (x, y) in pieza:
        tx = px + x
        ty = py + y
        if 0 <= ty < alto and 0 <= tx < ancho:
            tablero[ty][tx] = 1

# Rotación
def rotar(pieza):
    nueva = []
    for (x, y) in pieza:
        nueva.append((-y, x))
    return nueva

def ajustar_pieza(tablero, pieza, px, py):
    desplazamiento = [0, -1, 1, -2, 2]
    for d in desplazamiento:
        if not colision_pieza(tablero, pieza, px + d, py):
            return px + d, py
    return px, py

# Limpiar líneas completas
def limpiar_lineas(tablero):
    nuevo = []
    eliminadas = 0

    for fila in tablero:
        if all(c == 1 for c in fila):
            eliminadas += 1
        else:
            nuevo.append(fila)

    for _ in range(eliminadas):
        nuevo.insert(0, [0] * ancho)

    return nuevo, eliminadas

# Nueva pieza aleatoria
def nueva_pieza_aleatoria():
    indice = random.randint(0, len(PIEZAS) - 1)
    pieza = PIEZAS[indice]
    nombre = NOMBRES_PIEZAS[indice]
    return [(x, y) for (x, y) in pieza], nombre

# Puntajes
def puntaje_por_lineas(p):
    if p == 0: return 0
    if p == 1: return 100
    if p == 2: return 300
    if p == 3: return 500
    return 800

def guardar_puntaje(nombre, puntaje):
    try:
        with open(archivo_puntajes, "a", encoding="utf-8") as f:
            f.write(nombre + "," + str(puntaje) + "\n")
    except:
        print("Error al guardar puntaje.")

def top_tres_puntajes():
    lista = []

    try:
        with open(archivo_puntajes, "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split(",")
                if len(partes) != 2:
                    continue

                nombre = partes[0]
                try:
                    score = int(partes[1])
                except:
                    continue

                lista.append((nombre, score))
    except:
        return []

    lista.sort(key=lambda x: x[1], reverse=True)
    return lista[:3]

# Menú principal
def menu_principal():
    while True:
        limpiar_pantalla()
        print("===== PYTHON TETRIS =====\n")
        print("1. Jugar")
        print("2. Ver Top 3 puntajes")
        print("3. Salir\n")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            return "jugar"
        elif opcion == "2":
            return "top"
        elif opcion == "3":
            return "salir"
        else:
            input("Opción inválida. Presiona Enter para continuar...")

# Juego principal
def juego():
    tablero = crear_tablero()
    puntaje = 0
    tick = ticket_inicial

    pieza, nombre_p = nueva_pieza_aleatoria()
    px = ancho // 2
    py = -1

    while True:
        imprimir_tablero(tablero, pieza, px, py, puntaje)
        accion = input("Accion: ").strip().lower()

        if accion == "a":
            if not colision_pieza(tablero, pieza, px - 1, py):
                px -= 1

        elif accion == "d":
            if not colision_pieza(tablero, pieza, px + 1, py):
                px += 1

        elif accion == "s":
            if not colision_pieza(tablero, pieza, px, py + 1):
                py += 1

        elif accion == "w":
            pieza_rotada = rotar(pieza)
            npx, npy = ajustar_pieza(tablero, pieza_rotada, px, py)
            if not colision_pieza(tablero, pieza_rotada, npx, npy):
                pieza = pieza_rotada
                px = npx
                py = npy

        # Caída automática
        if not colision_pieza(tablero, pieza, px, py + 1):
            py += 1
        else:
            agregar_pieza_tablero(tablero, pieza, px, py)

            tablero, lineas = limpiar_lineas(tablero)
            if lineas > 0:
                puntaje += puntaje_por_lineas(lineas)
                tick = max(0.05, tick * (0.95 ** lineas))

            pieza, nombre_p = nueva_pieza_aleatoria()
            px = ancho // 2
            py = -1

            # GAME OVER
            if colision_pieza(tablero, pieza, px, py):
                imprimir_tablero(tablero, None, 0, 0, puntaje)
                print("Game Over!!!")
                print("Tu puntaje es:", puntaje)

                nombre = input("Nombre del jugador: ").strip()
                if nombre == "":
                    nombre = "Anonimo"

                guardar_puntaje(nombre, puntaje)

                print("\nTop 3 puntajes:")
                top = top_tres_puntajes()
                for i, (n, s) in enumerate(top, start=1):
                    print(i, ".", n, "-", s)

                print("\n¿Quieres jugar otra vez?")
                print("s = sí")
                print("n = no")

                opcion = input("Elige: ").strip().lower()

                if opcion == "s":
                    return "otra_vez"
                else:
                    return

        time.sleep(tick)

# Ejecución del programa
if __name__ == "__main__":
    while True:
        eleccion = menu_principal()

        if eleccion == "jugar":
            resultado = juego()
            if resultado == "otra_vez":
                juego()

        elif eleccion == "top":
            limpiar_pantalla()
            print("===== TOP 3 PUNTAJES =====\n")
            top = top_tres_puntajes()

            if not top:
                print("No hay puntajes aún.")
            else:
                for i, (n, s) in enumerate(top, start=1):
                    print(i, ".", n, "-", s)

            input("\nPresiona Enter para volver al menú...")

        elif eleccion == "salir":
            print("Gracias por jugar. ¡Hasta pronto!")
            break
