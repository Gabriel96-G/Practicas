# ===== Ejercicio 8: Sumar los dígitos de un número =====
# Este programa recibe un número entero positivo
# y calcula la suma de todos sus dígitos.

# Entrada de datos
numero = int(input("Ingrese un número entero positivo: "))

# Validación
if numero < 0:
    print("\nError: Debe ingresar un número positivo.")
else:
    suma = 0
    temp = numero  # Guardamos el valor original para mostrarlo al final

    # Bucle para extraer y sumar los dígitos
    while numero > 0:
        digito = numero % 10     # Obtiene el último dígito
        suma += digito           # Lo suma al acumulador
        numero //= 10            # Elimina el último dígito

    # Salida del resultado
    print(f"\nLa suma de los dígitos de {temp} es: {suma}")
