# ===== Ejercicio 10: Verificar si un número es primo =====

n = int(input("Ingresa un número entero: "))

if n <= 1:
    print("No es un número primo.")
else:
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break

    if primo:
        print(f"{n} es un número primo.")
    else:
        print(f"{n} no es un número primo.")