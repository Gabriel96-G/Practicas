#Declaracion de variables
numero1 = 0
numero2 = 0

#Entrada de datos
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

#Procesamiento de datos
if numero1 > numero2:
    print(f"El numero 1 es mayor")
elif numero1 == numero2:
    print(f"Los numeros son iguales")
else:
    print(f"El numero 2 es mayor")
