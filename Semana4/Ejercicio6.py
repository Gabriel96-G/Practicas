"""  Declarar Variables
Leer_num1
Leer_num2
Leer_Operacion

Operacion
Si operacion = "+" entonces
    resultado = num1 + num2
Si operacion = "-" entonces
    resultado = num1 - num2
Si operacion = "*" entonces
    resultado = num1 * num2
Si operacion = "/" entonces
    resultado = num1 / num2

"""
# Declaracion de variables
num1 = 0
num2 = 0
resultado = 0
operacion = ""
# Entrada de datos
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
operacion = input("Ingrese la operacion (+, -, *, /): ")
# Proceso
if operacion == "+":
    resultado = num1 + num2
if operacion == "-":
    resultado = num1 - num2
if operacion == "*":
    resultado = num1 * num2
if operacion == "/":
    resultado = num1 / num2
# Salida de datos
print(f"El resultado de la operacion es: {resultado}")  

