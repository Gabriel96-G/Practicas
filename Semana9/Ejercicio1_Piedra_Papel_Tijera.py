from __future__ import annotations
import random
from typing import Literal

# === Bloque de la imagen (se ejecuta una vez al iniciar el script) ===
opcion_computadora = random.randint(1, 3)
print(f"La opcion de la computadora es: {opcion_computadora}")
# =====================================================================

Opcion = Literal["piedra", "papel", "tijeras"]

OPCIONES_VALIDAS: tuple[Opcion, ...] = ("piedra", "papel", "tijeras")
REGLAS_GANAR: dict[Opcion, Opcion] = {
    "piedra": "tijeras",
    "tijeras": "papel",
    "papel": "piedra",
}

def normalizar_entrada(texto: str) -> str:
    """
    Limpia y normaliza la entrada del usuario.
    Permite también 'tijera' (singular).
    """
    t = texto.strip().lower()
    if t == "tijera":
        t = "tijeras"
    return t

def jugador_elegir() -> Opcion:
    """
    Pide la elección al jugador y valida la entrada.
    Retorna una de: "piedra", "papel" o "tijeras".
    """
    while True:
        eleccion_raw = input("Elige tu opción (piedra, papel o tijeras): ")
        eleccion = normalizar_entrada(eleccion_raw)
        if eleccion in OPCIONES_VALIDAS:
            return eleccion  # type: ignore[return-value]
        print("Entrada no válida. Intenta de nuevo escribiendo 'piedra', 'papel' o 'tijeras'.")

def computadora_elegir() -> Opcion:
    """
    Genera una opción aleatoria para la computadora usando randint,
    imprime el número (1-3) y lo mapea a la opción textual.
    """
    opcion_computadora = random.randint(1, 3)
    print(f"La opcion de la computadora es: {opcion_computadora}")
    mapeo = {1: "piedra", 2: "papel", 3: "tijeras"}
    return mapeo[opcion_computadora]  # type: ignore[return-value]

def determinar_ganador(jugador: Opcion, computadora: Opcion) -> str:
    """
    Determina el ganador según las reglas.
    Retorna: "jugador", "computadora" o "empate".
    """
    if jugador == computadora:
        return "empate"
    if REGLAS_GANAR[jugador] == computadora:
        return "jugador"
    return "computadora"

def jugar() -> None:
    """
    Lógica principal del juego:
      - Muestra instrucciones
      - Pide elección del jugador y de la computadora
      - Determina y muestra el resultado
      - Pregunta si se desea jugar nuevamente
    """
    print("=== Piedra, Papel o Tijeras ===")
    print("Reglas: Piedra > Tijeras, Tijeras > Papel, Papel > Piedra.\n")

    while True:
        jugador = jugador_elegir()
        computadora = computadora_elegir()

        print(f"\nTú elegiste: {jugador.capitalize()}")
        print(f"La computadora eligió: {computadora.capitalize()}")

        resultado = determinar_ganador(jugador, computadora)
        if resultado == "empate":
            print("Resultado: ¡Empate!\n")
        elif resultado == "jugador":
            print("Resultado: ¡Ganaste!\n")
        else:
            print("Resultado: Perdiste.\n")

        otra = input("¿Quieres jugar de nuevo? (s/n): ").strip().lower()
        if otra not in ("s", "si", "sí"):
            print("¡Gracias por jugar!")
            break

if __name__ == "__main__":
    jugar()