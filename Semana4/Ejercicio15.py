"""# Ejercicio 6: Elección del menú en un restaurante

# Declaración de variables
opcion = 0
platillo = ""

# Entrada de datos
try:
    opcion = int(input("Seleccione una opción del menú (1 = Entrada, 2 = Plato principal, 3 = Postre): "))

    # Proceso
    if opcion == 1:
        platillo = "Entrada: Sopa de verduras"
    elif opcion == 2:
        platillo = "Plato principal: Pollo a la plancha con ensalada"
    elif opcion == 3:
        platillo = "Postre: Flan de vainilla"
    else:
        platillo = "Opción inválida. Elija entre 1, 2 o 3."

    # Salida
    print(platillo)

except:
    print("Ingrese un número válido (1, 2 o 3)")
"""
# Ejercicio 6: Elección del menú en un restaurante
# Declaración de variables
opcion = 0
platillo = ""   
# Entrada de datos
try:        
    opcion = int(input("Seleccione una opción del menú (1 = Entrada, 2 = Plato principal, 3 = Postre): "))   
    # Proceso
    if opcion == 1:
        platillo = "Entrada: Sopa de verduras"
    elif opcion == 2:
        platillo = "Plato principal: Pollo a la plancha con ensalada"
    elif opcion == 3:
        platillo = "Postre: Flan de vainilla"
    else:
        platillo = "Opción inválida. Elija entre 1, 2 o 3."
    # Salida
    print(platillo)

except:
    print("Ingrese un número válido (1, 2 o 3)")

    