# ===== Ejercicio 7: Calcular el factorial de un número =====
# Este programa recibe un número entero positivo N
# y calcula su factorial usando un bucle.
# Ejemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120

# Entrada de datos
N = int(input("Ingrese un número entero positivo: "))

# Validación
if N < 0:
    print("\nError: El número debe ser positivo.")
else:
    factorial = 1  # Variable para almacenar el resultado

    # Bucle para calcular el factorial
    for i in range(1, N + 1):
        factorial *= i

    # Salida del resultado
    print(f"\nEl factorial de {N} es: {factorial}")
