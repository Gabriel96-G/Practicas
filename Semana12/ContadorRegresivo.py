""" 
1. Contador regresivo
Crear una función recursiva que imprima los números desde n hasta 1
"""

def contador_regresivo(n):
    # Caso base: si n es menor que 1, detener la recursión
    if n == 0:
        print(0)
        return
    # Imprimir el número actual
    
    print(n)
    # Llamada recursiva con n-1
    contador_regresivo(n - 1)

def main():
    entrada = input("Ingrese un número entero positivo para el contador regresivo: ")
    try:
        n = int(entrada)
        if n < 0:
            print("Por favor, ingrese un número entero positivo.")
            return
        contador_regresivo(n)
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero positivo.")

if __name__ == "__main__":
    main()

    