# ===== Ejercicio 6: Imprimir los números impares entre dos valores =====
# Este programa recibe dos números A y B (donde A < B)
# y muestra todos los números impares que existen entre ellos.

# Entrada de datos
A = int(input("Ingrese el valor de A (menor): "))
B = int(input("Ingrese el valor de B (mayor): "))

# Validación de rango
if A < B:
    print(f"\nLos números impares entre {A} y {B} son:")

    # Bucle para recorrer los números del rango
    for numero in range(A, B + 1):
        # Verificar si el número es impar
        if numero % 2 != 0:
            print(numero)

else:
    print("\nError: El valor de A debe ser menor que el de B.")
