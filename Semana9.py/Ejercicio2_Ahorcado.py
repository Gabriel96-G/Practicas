
"""
Ahorcado (Hangman) — versión consola
Cumple con la especificación solicitada:
- Selección aleatoria de palabra de una lista predefinida.
- Adivinanza por letras con validación de entrada.
- Intentos limitados (7).
- Muestra progreso, intentos restantes y letras usadas.
- Finaliza al adivinar toda la palabra o al agotar intentos.
- Opción de volver a jugar.
"""

from __future__ import annotations
import random
from typing import List, Set

# ======== Configuración ========
INTENTOS_MAX = 7

# Lista de palabras (solo minúsculas para simplificar validación)
# Puedes ampliar esta lista libremente.
PALABRAS: List[str] = [
    "python", "ingenieria", "sistema", "algoritmo", "variable",
    "funcion", "clase", "modulo", "archivo", "depuracion",
    "consola", "proceso", "modelo", "datos", "testing",
    "calidad", "metrica", "agil", "scrum", "kanban"
]

# Etapas del ahorcado (0 errores hasta INTENTOS_MAX errores)
HANGMANPICS = [
    r"""
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    """,
]

ALFABETO: Set[str] = set("abcdefghijklmnopqrstuvwxyzñ")

# ======== Funciones principales ========
def elegir_palabra() -> str:
    """Selecciona una palabra aleatoria de la lista predefinida."""
    return random.choice(PALABRAS)

def mostrar_palabra(palabra_secreta: str, letras_adivinadas: Set[str]) -> str:
    """
    Devuelve la palabra con letras reveladas y guiones bajos en lo no adivinado.
    Ej.: 'p_y_h_n' (se separa por espacios al imprimir para mejor lectura).
    """
    return " ".join([c if c in letras_adivinadas else "_" for c in palabra_secreta])

def pedir_letra(letras_usadas: Set[str]) -> str:
    """
    Solicita una letra válida al usuario:
    - Debe ser una sola letra del alfabeto español básico (a-z, ñ).
    - No debe haberse usado antes.
    """
    while True:
        entrada = input("Ingresa una letra: ").strip().lower()
        if len(entrada) != 1 or entrada not in ALFABETO:
            print("Entrada inválida. Debes ingresar una sola letra (a-z o ñ).")
            continue
        if entrada in letras_usadas:
            print(f"Ya usaste la letra '{entrada}'. Prueba otra.")
            continue
        return entrada

def jugar() -> None:
    """Controla el flujo del juego Ahorcado."""
    palabra = elegir_palabra()
    letras_correctas: Set[str] = set()
    letras_usadas: Set[str] = set()
    errores = 0
    letras_objetivo = set(palabra)  # letras únicas de la palabra

    print("\n=== AHORCADO ===")
    while errores < INTENTOS_MAX and not letras_objetivo.issubset(letras_correctas):
        # Mostrar estado
        print(HANGMANPICS[min(errores, len(HANGMANPICS) - 1)])
        print("Palabra: ", mostrar_palabra(palabra, letras_correctas))
        print(f"Intentos restantes: {INTENTOS_MAX - errores}")
        print("Letras usadas: ", " ".join(sorted(letras_usadas)) if letras_usadas else "-")

        # Pedir letra
        letra = pedir_letra(letras_usadas)
        letras_usadas.add(letra)

        if letra in letras_objetivo:
            letras_correctas.add(letra)
            print(f"¡Bien! La letra '{letra}' está en la palabra.\n")
        else:
            errores += 1
            print(f"Fallaste. La letra '{letra}' no está en la palabra.\n")

    # Resultado final
    exito = letras_objetivo.issubset(letras_correctas)
    print(HANGMANPICS[min(errores, len(HANGMANPICS) - 1)])
    if exito:
        print("¡Felicidades! Adivinaste la palabra:", palabra)
    else:
        print("Has perdido. La palabra era:", palabra)

def main() -> None:
    while True:
        jugar()
        otra = input("\n¿Quieres jugar otra vez? (s/n): ").strip().lower()
        if otra != "s":
            print("¡Gracias por jugar!")
            break

if __name__ == "__main__":
    main()
