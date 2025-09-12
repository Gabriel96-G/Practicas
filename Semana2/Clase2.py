x = 5
y = 10
z = x + y
print(z)

################################

def suma(a, b):
    #variable local
    a = 10
    b = 20
################################

saludo = "Hola"
n = 10
pi = 3.1416
lista = [1, 2, 3, 4, 5]
dos_palabras = "Hola Mundo"   #SnakeCase
dospalabras="HolaMundo" #CamelCase

################################

#Esto es un comentario de una sola línea

"""
Este es mi programa en Python.
El programa debe solictar al usuarion tres números enteros
Autor: Ale24
Fecha: 11/03/2024

"""
# ============= Variables ==================
n1 = 10 # Estos es una variable que almacena el valor del primer numero
n2 = 20 # Estos es una variable que almacena el valor del segundo numero
n3 = 30 # Estos es una variable que almacena el valor del tercer numero 
resultadoSuma = n1 + n2 + n3 # Esta variable almacena el resultado de la suma de los tres numeros
resultadoMultiplicacion = n1 * n2 * n3 # Esta variable almacena el resultado de la multiplicacion de los tres numeros

"""
Entrada de Datos:
Se utiliza la función input() para solicitar al usuario que ingrese tres números enteros.
Ejemplo:
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: ")) 
numero3 = int(input("Ingrese el tercer número entero: "))



Para salida de Datos: Se utiliza la función print() para mostrar los resultados de la suma y multiplicación de los tres números

"""
# ============= Entrada de Datos ==================
numero1 = int(input("ingrese el primer número entero: "))
numero2 = int(input("ingrese el segundo número entero: "))
numero3 = int(input("ingrese el tercer número entero: "))

# ============= Procesamiento de Datos ==================
resultadoSuma = numero1 + numero2 + numero3
resultadoMultiplicacion = numero1 * numero2 * numero3

print("El resultado de la suma es: ", resultadoSuma)
print("El resultado de la multiplicación es: ", resultadoMultiplicacion)

print("El resultado de la suma es: " + str(resultadoSuma))
print("El resultado de la multiplicación es: ", resultadoMultiplicacion)


Se necesita una conversión de tipos de datos para asegurar que los valores ingresados por el usuario sean tratados como enteros.

"""
#Concatenacion de Texto
print("El resultado de la suma es: " + str(resultadoSuma))
# Concatenacion de Texto y Variable
print("El resultado de la multiplicación es: ", resultadoMultiplicacion)

"""














