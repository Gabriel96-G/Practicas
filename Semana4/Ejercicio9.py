"""
Declarar variables

temperatura_menor_0 = "Frio extremo"
temperatura_entre_0_y_10 = "Clima templado"
temperatura_mayor_30 = "Calor intenso"


Imprimir la temperatura a grados celsius
"""

#Declarar variables
temperatura_menor_0 = "Frio extremo"
temperatura_entre_0_y_10 = "Clima templado"
temperatura_mayor_30 = "Calor intenso"

#Entrada de datos
temperatura = float(input("Ingrese la temperatura en grados Celsius: "))    
#Proceso
if temperatura < 0: 
    print(temperatura_menor_0)
elif temperatura >= 0 and temperatura <= 10:    
    print(temperatura_entre_0_y_10)
elif temperatura > 30:
    print(temperatura_mayor_30)
#Salida de datos
else:
    print("Clima agradable")
    