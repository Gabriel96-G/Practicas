# ===== Ejercicio 9: Encontrar el mayor de un conjunto de números =====

"""
# Ejercicio 9: Encontrar el mayor de un conjunto de números
Pedir la cantidad de números
Verificar que la cantidad sea positiva
leer los N números
"""

n = int(input("¿Cuántos números vas a ingresar? "))

if n > 0:
    mayor = int(input("Ingresa un número: "))

    for i in range(n - 1):
        num = int(input("Ingresa otro número: "))
        if num > mayor:
            mayor = num

    print(f"El número mayor es: {mayor}")
else:
    print("Error: Debes ingresar una cantidad positiva.")

