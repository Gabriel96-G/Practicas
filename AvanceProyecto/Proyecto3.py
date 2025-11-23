import random
import time
import os

# Constantes del juego Tetris
ancho = 10
alto = 20
ticket_inicial = 1
puntajes = "scores.txt"

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

# Utilidades de Tetris
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def crear_tablero():
    tablero = []
    for _ in range(alto):
        fila = [0] * ancho
        tablero.append([0] * ancho)
    return tablero

def copiar_lista(l):
    return [list(row) for row in l]

# Dibujar tablero
def imprimir_tablero(tablero, pieza = None, px=0, py=0, puntuacion=0):
    copia = copiar_lista(tablero)
    if pieza: 
        for (x, y) in pieza:
            tx = px + x
            ty = py + y
            if 0 <= ty < alto and 0 <= tx < ancho:
                copia[ty][tx] = 1  # Marca la pieza actual
    limpiar_pantalla()
    print("puntaje:", puntuacion)
    print("+" + "-" * ancho + "+")
    for fila in copia:
        linea = "|"
        for celda in fila:
            linea += "#" if celda else " "
        linea += "|"
        print(linea)
    print("+" + "-" * ancho + "+")
    print("controles: a=izquierda, d=derecha, s=abajo, w=rotar, [enter]=nada")

# Colocación y colision de piezas
def coalision_pieza(tablero, pieza, px, py):
    for (x, y) in pieza:
        tx = px + x
        ty = py + y
        if tx < 0 or tx >= ancho or ty < 0 or ty >= alto:
            return True
        if ty >= 0 and tablero[ty][tx] == 1:
            return True
    return False

def agregar_pieza_tablero(tablero, pieza, px, py):
    for (x, y) in pieza:
        tx = px + x
        ty = py + y
        if 0 <= ty < alto and 0 <= tx < ancho:
            tablero[ty][tx] = 1

# Rotación y ajuste de piezas
def rotar(pieza):
    nueva = []
    for (x, y) in pieza:
        nueva.append((-y, x))
    return nueva

def ajustar_pieza(tablero, pieza, px, py):
    desplazamiento = [0, -1, 1, -2, 2]
    for d in desplazamiento:
        if not coalision_pieza(tablero, pieza, px + d, py):
            return px + d, py
    return px, py

# Limpiar líneas
def limpiar_lineas(tablero):
    nuevo = []
    elimianadas = 0
    for fila in tablero:
        if all (celda == 1 for celda in fila):
            elimianadas += 1
        else:
            nuevo.append(fila)
    for _ in range(elimianadas):
        nuevo.insert(0, [0] * ancho)
    return nuevo, elimianadas

# Generar pieza
def nueva_pieza_aleatoria():
    indice = random.randint(0, len(PIEZAS))
    pieza = [indice]
    nombre = [indice]
    return [ (x, y) for (x, y) in pieza ], nombre

# Puntaje
def puntaje_por_lineas(p):
    if p == 0: return 0
    if p == 1: return 100
    if p == 2: return 300
    if p == 3: return 500
    return 800

def guardar_puntaje(nombre, puntaje):
    try:
        with open(puntajes, "a", encoding="utf-8") as f:
            f.write(f"{nombre},{puntaje}\n")
    except Exception as e:
        print("Error al guardar puntaje:")

def top_tres_puntajes():
    lista = []
    try:
        with open(puntajes, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split(",")
                if len(partes) != 2:
                    continue
                nombre = partes[0]
                try:
                    score = int(partes[1])
                except:
                    continue
                lista.append((nombre, score))
    except FileNotFoundError:
        return []
    lista.sort(key=lambda x: x[1], reverse=True)
    return lista[:3]

def 












