# Declaracion de variables

Kilometro_Antes = 0.0
Kilometro_Despues = 0.0
Diferencia_de_Distancia = 0.0


# Entrada de datos
Kilometro_Antes = float(input("Ingrese los kilómetros recorridos antes del servicio: "))
Kilometro_Despues = float(input("Ingrese los kilómetros recorridos después del servicio: "))

# Operaciones
Diferencia_de_Distancia = Kilometro_Despues - Kilometro_Antes

# Salida de datos
print(f"La diferencia de distancia recorrida es: {Diferencia_de_Distancia:.2f} km")
