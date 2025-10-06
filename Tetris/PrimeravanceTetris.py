# Programa 1: Estado del juego según apilamiento
# Reglas:
# - Entrada debe ser un número entero POSITIVO.
# - Si < 20  -> "Juego en curso"
# - Si == 20 -> "Jugador ha perdido la partida"
# - Si > 20  -> "Dato de entrada no válido"
# - Si es negativo, decimal o no numérico -> "Dato de entrada no válido"

def es_entero_positivo(s: str) -> bool:
    if s.strip().startswith("+"):
        s = s.strip()[1:]
    return s.isdigit() and int(s) > 0

def main():
    dato = input("Ingrese el apilamiento (entero positivo): ").strip()
    if not es_entero_positivo(dato):
        print("Dato de entrada no válido")
        return
    n = int(dato)
    if n < 20:
        print("El juego se encuentra en curso")
    elif n == 20:
        print("El jugador ha perdido la partida")
    else:  # n > 20
        print("Dato de entrada no válido")

if __name__ == "__main__":
    main()


# Programa 2: Puntaje f(N) = (5/2) * N * (N + 1) para 0 ≤ N ≤ 50
# Reglas de validación:
# - Entrada debe ser un número ENTERO
# - Si N < 0, N > 50, decimal o no numérico -> "Dato de entrada no válido"
# - En rango [0, 50]: imprimir resultado de f(N)
#
# Nota matemática: N*(N+1) es par, por lo que f(N) es entero.
def es_entero(s: str) -> bool:
    s = s.strip()
    if s.startswith(("+","-")):
        s = s[1:]
    return s.isdigit()

def main():
    dato = input("Ingrese cantidad_lineas (entero entre 0 y 50): ").strip()
    if not es_entero(dato):
        print("Dato de entrada no válido")
        return
    N = int(dato)
    if N < 0 or N > 50:
        print("Dato de entrada no válido")
        return
    # f(N) entero sin errores de coma flotante
    fN = (5 * N * (N + 1)) // 2
    print(f"f(N) = {fN}")

if __name__ == "__main__":
    main()



# Programa 3: Impresión de piezas Tetris con asteriscos
# Caracter válido: uno de {'o','l','s','z','L','J','T'}
# Cualquier otro valor -> "Dato de entrada no válido"
#
# Convenciones:
# - 'o'  -> O (cuadrado 2x2)
# - 'l'  -> I (línea horizontal de 4)  [la consigna usa 'l' minúscula]
# - 's', 'z' -> zigzags
# - 'L', 'J' -> piezas en L
# - 'T'      -> pieza T
# Cada figura se almacena como str.

pieza_o = (
    "****\n"
    "****"
)

pieza_l = (
    "****"
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
    "***\n"
    " * "
)

PIEZAS = {
    'o': pieza_o,
    'l': pieza_l,
    's': pieza_s,
    'z': pieza_z,
    'L': pieza_L,
    'J': pieza_J,
    'T': pieza_T,
}

def main():
    ch = input("Ingrese una letra de pieza (o, l, s, z, L, J, T): ")
    if len(ch) != 1 or ch not in PIEZAS:
        print("Dato de entrada no válido")
        return
    print(PIEZAS[ch])

if __name__ == "__main__":
    main()
