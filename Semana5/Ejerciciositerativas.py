# Ejercicio 1
"""
Se va a recibir un numero entero, y obtener la suma total de sus digitos.
123 -> 1 + 2 + 3 = 6
"""

numero = int(input("Ingrese un numero entero: "))
suma_digitos = 0
# 123 -> 3
x = numero % 10
while numero > 0:
    suma_digitos += x
    numero = numero // 10
    x = numero % 10
print(suma_digitos)

numero = input("Ingrese un numero entero: ")
suma_digitos = 0

if numero.isdigit():
    for i in range(len(numero)):
        suma_digitos += int(numero[i])
    print(suma_digitos)
else:
    print("No es un numero entero")


# Ejercicio 2
"""
Vamos a escribir un programa que imprima un mensaje final, solo si el usuario digita un 0
"""
# opcion = int(input("Escriba una opcion o digite 0 para salir: "))

# while opcion != 0:
#     print("Estoy atrapado! Aiuuuddaaa!")
#     opcion = int(input("Escriba una opcion o digite 0 para salir: "))
# print("Ganamos! Salimos del ciclo!")

menu = "Bienvenido a mi sistema" \
"1. Para registrar usuario\n" \
"2. Para Modificar usuario\n" \
"3. Para eliminar usuario\n" \
"0. Para salir"

print(menu)

opcion = int(input("\nIngrese una opcion del menu: "))

while opcion != 0:
    if opcion == 1:
        print("Registrando usuario...")
    elif opcion == 2:
        print("Modificando usuario...")
    elif opcion == 3:
        print("Eliminando usuario...")
    else:
        print("Opción invalida")
    opcion = int(input("Escriba una opcion o digite 0 para salir: "))
print("Ganamos! Salimos del ciclo!")

# Ejercicio 3
"""

"""
