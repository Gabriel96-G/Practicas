numero = int(input("Ingrese un número entero positivo: "))

if numero > 0:
    suma = 0

    while numero > 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    print(f"La suma de los digítos es: {suma}")
else:
    print("Error, se debe ingresar un número entero positivo")