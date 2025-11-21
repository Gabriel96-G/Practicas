# Recursividad
# Es una funcion que se llama a si misma, sirve para resolver problemas que se pueden dividir en subproblemas
# La recursion tiene 3 bases fundamentales:
# 1. Caso Base o Condicion de parada: Es el que permite que la recursion termine
# 2. Movimiento de avance: Es el que permite que la recursion se mueva hacia el caso base
# 3. Llamada recursiva: Es el que permite que la recursion se llame a si misma

# Ejemplo de recursion:
# No tenemos caso base, no hay movimiento de avance
contador = 0
while True:
    print(contador)

# Tenemos un caso base, pero no hay movimiento de avance

contador = 0
while True:
    if contador >= 10:
        break
    print(contador)

# Tenemos un caso base, y hay movimiento de avance
contador = 0
while True:
    if contador >= 10: # Caso base
        break
    print(contador)
    contador += 1 # Movimiento de avance

# Ejemplo de recursion:
# Definimos la funcion factorial
# Definimos un caso base
# Definimos un movimiento de avance -> va con la llamada recursiva
def factorial(n):
    if n == 0: # Caso base o condicion de finalizacion
        return 1
    return n * factorial(n-1) #llamada recursiva

# 5 * factorial(4) -> 
# 5 * 4 * factorial(3) -> 
# 5 * 4 * 3 * factorial(2) -> 
# 5 * 4 * 3 * 2 * factorial(1) -> 



import turtle

def dibujar_espiral(tortuga, largo_linea):
    if largo_linea >= 500:   #Caso Base
        return
    tortuga.forward(largo_linea)
    tortuga.right(93)
    dibujar_espiral(tortuga, largo_linea + 20)

tortuga = turtle.Turtle(shape="turtle")
tortuga.pensize(2)
tortuga.color("red")
dibujar_espiral(tortuga, 5)
turtle.done()

# 5 * 4 * 3 * 2 * 1 * factorial(0) -> 
# 5 * 4 * 3 * 2 * 1 * 1 -> 120