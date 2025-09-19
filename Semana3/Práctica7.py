# Declaracion de variables
Nombre_de_Pais = ""
Cantidad_de_Enfermos = 0
Cantidad_de_Muertos = 0
Tasa_de_Mortalidad = 0.0

# Entrada de datos
Nombre_de_Pais = input("Ingrese el nombre del país: ")
Cantidad_de_Enfermos = int(input("Ingrese la cantidad de enfermos: "))
Cantidad_de_Muertos = int(input("Ingrese la cantidad de muertos: "))


# Operaciones
Tasa_de_Mortalidad = (Cantidad_de_Muertos / Cantidad_de_Enfermos) * 100

# Salida de datos   
print(f"Nombre del país: {Nombre_de_Pais} , Tasa de mortalidad calculada: {Tasa_de_Mortalidad:.2f}%") 



