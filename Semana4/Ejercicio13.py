"""# Ejercicio 4: Calcular impuestos según el salario

# Declaración de variables
salario = 0.0
impuesto = 0.0

# Entrada de datos
try:
    salario = float(input("Ingrese el salario del trabajador: "))

    # Proceso
    if salario < 1000:
        impuesto = 0
    elif salario <= 2000:
        impuesto = salario * 0.10
    else:
        impuesto = salario * 0.20

    # Salida
    print(f"El salario es: ${salario:.2f}")
    print(f"El impuesto a pagar es: ${impuesto:.2f}")

except:
    print("Ingrese un valor numérico válido para el salario")

"""
# Ejercicio 4: Calcular impuestos según el salario
# Declaración de variables  
salario = 0.0
impuesto = 0.0      
# Entrada de datos
try:        
    salario = float(input("Ingrese el salario del trabajador: "))   
    # Proceso
    if salario < 1000:
        impuesto = 0
    elif salario <= 2000:
        impuesto = salario * 0.10
    else:
        impuesto = salario * 0.20
    # Salida
    print(f"El salario es: ${salario:.2f}")
    print(f"El impuesto a pagar es: ${impuesto:.2f}")
except:
    print("Ingrese un valor numérico válido para el salario")