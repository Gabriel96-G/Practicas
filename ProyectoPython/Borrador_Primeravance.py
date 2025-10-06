# ===== Programa 1: Estado del juego según apilamiento =====

# Declaración de variables
apilamiento = 0

# Entrada de datos + validación
dato = input("Ingrese el apilamiento (entero positivo): ")

# Proceso y salida
try:
    apilamiento = int(dato)
    if apilamiento <= 0:
        print("Dato de entrada no válido")
    elif apilamiento < 20:
        print("El juego se encuentra en curso")
    elif apilamiento == 20:
        print("El jugador ha perdido la partida")
    else:  # apilamiento > 20
        print("Dato de entrada no válido")
except ValueError:
    # Cubre decimales y texto no numérico
    print("Dato de entrada no válido")


# ===== Programa 2: Puntaje acumulado =====

# Declaración de variables
N = 0
fN = 0

# Entrada de datos
dato = input("Ingrese cantidad_lineas (entero entre 0 y 50): ")

# Proceso y salida
try:
    N = int(dato)
    if N < 0 or N > 50:
        print("Dato de entrada no válido")
    else:
        # f(N) = (5/2) * N * (N + 1)
        # Se usa // 2 para asegurar que el resultado sea un número entero
        fN = (5 * N * (N + 1)) // 2
        print("f(N) =", fN)
except ValueError:
    print("Dato de entrada no válido")

# ===== Programa 3: Impresión de piezas Tetris =====

# Declaración de variables (cada pieza como str)
pieza_o = (
    "****\n"
    "*  *\n"
    "*  *\n"
    "****"
)

pieza_l = (
    "* \n"
    "* \n"
    "* \n"
    "*"
)

pieza_s = (
    " **\n"
    "** "
)

pieza_z = (
    "** \n"
    " **"
)

pieza_L = (
    "*  \n"
    "*  \n"
    "** "
)

pieza_J = (
    "  *\n"
    "  *\n"
    " **"
)

pieza_T = (
    "*****\n"
    "  * \n" \
    "  * "
)

# Entrada de datos
ch = input("Ingrese una letra de pieza (o, l, s, z, L, J, T): ")

# Proceso y salida (solo if/elif/else)
if len(ch) != 1:
    print("Dato de entrada no válido")
elif ch == "o":
    print(pieza_o)
elif ch == "l":
    print(pieza_l)
elif ch == "s":
    print(pieza_s)
elif ch == "z":
    print(pieza_z)
elif ch == "L":
    print(pieza_L)
elif ch == "J":
    print(pieza_J)
elif ch == "T":
    print(pieza_T)
else:
    print("Dato de entrada no válido")


