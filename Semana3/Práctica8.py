# Declaracion de variables
Costo_de_Automovil_Nuevo = 0.0
Ganancia_del_Vendedor = 0.0
Impuesto = 0.0
Costo_de_Automovil = 0.0


# Entrada de datos
Costo_de_Automovil = float(input("Ingrese el costo del automóvil nuevo: "))



# Operaciones
Ganancia_del_Vendedor = Costo_de_Automovil * 0.15
Impuesto = Costo_de_Automovil * 0.30
Costo_de_Automovil_Nuevo = Costo_de_Automovil + Ganancia_del_Vendedor + Impuesto 


# Salida de datos
print(f"El costo del automóvil nuevo es: {Costo_de_Automovil_Nuevo}")
