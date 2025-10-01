"""
Declarar variables


edad_nino
edad_adolescente
edad_adulto

"""

# Programa para clasificar la categoría de edad

edad = int(input("Ingrese la edad: "))

if 0 <= edad <= 12:
    print("Niño")
elif 13 <= edad <= 17:
    print("Adolescente")
elif edad >= 18:
    print("Adulto")
else:
    print("Edad no válida")