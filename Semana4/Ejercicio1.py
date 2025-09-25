# Ejercicio 1
#Declaracion de variables
n = 0


#Entrada de datos
try:
    n = int(input("Ingrese un numero entero: "))

    if n % 2 == 0:
        print(f"Es par")
    else:
        print(f"Es impar")
    

except: 
 print("Ingrese un numero valido")