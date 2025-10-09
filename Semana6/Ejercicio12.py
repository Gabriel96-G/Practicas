# Ejercicio 12: Imprimir los primeros N números de la serie Fibonacci

N = int(input("Ingrese la cantidad de números de la serie Fibonacci: "))

if N > 0:
    a, b = 0, 1  
    print("Serie Fibonacci:")

    for i in range(N):
        print(a)
        a, b = b, a + b  
else:
    print("Error: Debe ingresar un número positivo.")