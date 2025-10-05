#Declaración de variables
suma_de_salarios = 0.0
salario1 = 0.0
salario2 = 0.0      
salario3 = 0.0
salario4 = 0.0
salario5 = 0.0
#Entrada de datos
salario1 = int(input("Ingrese el salario del empleado 1: "))   
salario2 = int(input("Ingrese el salario del empleado 2: "))
salario3 = int(input("Ingrese el salario del empleado 3: "))
salario4 = int(input("Ingrese el salario del empleado 4: "))
salario5 = int(input("Ingrese el salario del empleado 5: "))    

suma_total = salario1 + salario2 + salario3 + salario4 + salario5

suma_de_salarios = 0
salario = 0

for i in range(5): # [0, 1, 2, 3, 4]
    salario = int(input(f"Ingrese el salario del empleado {i + 1}: "))
    suma_de_salarios += salario

print(suma_total)
tupla = (1, 2, 3, 4, 5)
lista = [1, 2, 3, 4, 5]
lista = ["a", "b", "c", "d", "e"]
matriz = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
    ] 

# Acceso una lista
# [0, 1, 2, 3, 4, 5] 
lista[0] # 1
lista[2] # 3
lista[5] # Error
lista[-1] # 5
lista[-2] # 4   


text = "Hola"
text[0] # "h"


# Operaciones
lista.append(6) # Agrega un elemento al final de la lista
lista[0] = 10 # Modifica el valor en la posición 0
lista.pop()
lista.index()
lista.remove()

#Ejercicios
# Recibir una cadena de texto ingresada por el usuario y vamos a imprimirla al reves

texto = input("Ingrese un mensaje de texto: ")
texto_inverso = ""


for i in range(len(texto)):
    texto_inverso += texto[i *(-1)]


print(texto_inverso)



