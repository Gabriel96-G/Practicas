#Ejercicio3

##Declaración de variables
nota = 0

##Entrada de datos
try: 
    nota = int(input("Ingrese la nota: "))
    if nota >= 70 and nota <= 100 :
        print("Aprobó")
    elif nota >= 0 and nota < 70:
        print("Reprobó")
    else:
        print("Ingrese una nota valida")

except: 
    print("Ingrese un numero entre 0 y 100")

