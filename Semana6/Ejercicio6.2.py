# Ejercicio 6: Imprimir los números impares entre dos valores

A = int(input("Ingrese el valor de A (menor): "))
B = int(input("Ingrese el valor de B (mayor): "))

if A < B:
    print(f"Los números impares entre {A} y {B} son:")
    for numero in range(A, B + 1):
        if numero % 2 != 0:
            print(numero)
else:
    print("Error: El valor de A debe ser menor que el de B.")