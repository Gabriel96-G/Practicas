"""# Declarar las variables

imprimir_compra
descuento = 0
precio_final = 0

# si el total es >100 entonces (if) se aplica el descuento 

descuento = compra * 0.10

precio_final = compra - descuento
"""

# Declaracion de variables
compra = 0
descuento = 0
precio_final = 0

# Entrada de datos
compra = float(input("Ingrese el total de la compra: "))

# Proceso
if compra > 100:
    descuento = compra * 0.10
    precio_final = compra - descuento
else:
    precio_final = compra

# Salida de datos
print(f"El total de la compra es: {compra}")
print(f"El precio final es: {precio_final}")