"""
# Ejercicio 3: Determinar si un año es bisiesto con la fórmula lógica

# Declaración de variables
anio = 0
resultado = ""

# Entrada de datos
try:
    anio = int(input("Ingrese un año: "))

    # Proceso (aplicando la fórmula)
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        resultado = f"El año {anio} es bisiesto."
    else:
        resultado = f"El año {anio} no es bisiesto."

    # Salida
    print(resultado)

except:
    print("Ingrese un número válido para el año")
"""

# Ejercicio 3: Determinar si un año es bisiesto con la fórmula lógica
# Declaración de variables
anio = 0
resultado = ""      
# Entrada de datos
try:        
    anio = int(input("Ingrese un año: "))   
    # Proceso (aplicando la fórmula)
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        resultado = f"El año {anio} es bisiesto."
    else:
        resultado = f"El año {anio} no es bisiesto."
    # Salida
    print(resultado)
except:
    print("Ingrese un número válido para el año")
