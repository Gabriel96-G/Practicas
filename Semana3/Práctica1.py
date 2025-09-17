# Declaracion de variables
Impuesto = 13 / 100
Precio_de_Producto = 0.0
Nombre_de_Producto = ""
Precio_Final = 0.0

# Entrada de datos
Nombre_de_Producto = input("Ingrese el nombre del producto: ")
Precio_de_Producto = float(input("Ingrese el precio del producto: "))

# Operaciones
Precio_Final = Precio_de_Producto + (Precio_de_Producto * Impuesto)

# Salida de datos
print(f"El precio final de {Nombre_de_Producto} es: {Precio_Final:.2f}")