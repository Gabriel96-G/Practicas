"""
Declarar variables

num1 = "Domingo"
num2 = "Lunes"
num3 = "Martes"
num4 = "Miercoles"
num5 = "Jueves"
num6 = "Viernes"
num7 = "Sabado"

Imprimir el dia de la semana

print(num1) = Domingo
print(num2) = Lunes
print(num3) = Martes
print(num4) = Miercoles
print(num5) = Jueves
print(num6) = Viernes
print(num7) = Sabado




"""
#Declarar variables
num1 = "Domingo"
num2 = "Lunes"  
num3 = "Martes"
num4 = "Miercoles"
num5 = "Jueves"
num6 = "Viernes"
num7 = "Sabado"

#Entrada de datos
numero = int(input("Ingrese un número del 1 al 7: "))

#Proceso  

if numero == 1:
    print("Lunes")
elif numero == 2:
    print("Martes")
elif numero == 3:
    print("Miércoles")
elif numero == 4:
    print("Jueves")
elif numero == 5:
    print("Viernes")
elif numero == 6:
    print("Sábado")
elif numero == 7:
    print("Domingo")
else:
    print("Número inválido, por favor ingrese un número del 1 al 7.")
    
#Salida de datos

print("El día de la semana es:", num1 if numero == 1 else
      num2 if numero == 2 else
      num3 if numero == 3 else
      num4 if numero == 4 else
      num5 if numero == 5 else
      num6 if numero == 6 else
      num7 if numero == 7 else "Número inválido")