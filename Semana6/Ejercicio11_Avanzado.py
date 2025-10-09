# Ejercicio 11: Invertir un número

numero = int(input("Ingrese un número entero positivo: "))

if numero > 0:
    invertido = 0

    while numero > 0:
        digito = numero % 10           
        invertido = invertido * 10 + digito  
        numero //= 10                  

    print(f"El número invertido es: {invertido}")
else:
    print("Error: Debe ingresar un número entero positivo.")