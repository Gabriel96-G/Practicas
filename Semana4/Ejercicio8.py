"""
Variables

Ingresar_triangulo

Si los tres lados iguales entonces
Triangulo Equilatero
Si no los dos lados iguales y uno diferente entonces
Triangulo Isoceles
Si no los tres lados diferentes entonces
Triangulo Escaleno


Triangulo por Lado es,  Triangulo
"""

#Declarar variables
lado1 = float(input("Ingrese el primer lado del triangulo: "))
lado2 = float(input("Ingrese el segundo lado del triangulo: "))
lado3 = float(input("Ingrese el tercer lado del triangulo: "))
triangulo = ""
#Proceso
if lado1 == lado2 == lado3:
    triangulo = "Equilatero"
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    triangulo = "Isoceles"
else:
    triangulo = "Escaleno"

#Salida de datos
print(f"Triangulo por Lado es: {triangulo}")

