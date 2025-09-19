# Declaracion de variables
Salario_Bruto = 0.0
Impuesto = 0.0
Salario_Neto = 0.0

# Entrada de datos
Salario_Bruto = float(input("Ingrese el salario bruto: "))
Impuesto = float(input("Ingrese el porcentaje de impuesto : "))


# Operaciones

Salario_Neto = Salario_Bruto * (1 - Impuesto / 100)

# Salida de datos
print(f"El salario neto es: {Salario_Neto}")
