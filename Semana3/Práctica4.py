# Declaracion de variables
edad_de_la_abuela_de_Ana_Actual = 0
edad_del_abuelo_de_Ana = 25
anno_del_matrimonio = 0

# Entrada de datos

anno_del_matrimonio = int(input("Ingrese el año en que se casaron los abuelos de Ana: "))


# Operaciones
edad_de_la_abuela_de_Ana_Actual =  anno_del_matrimonio / ( edad_del_abuelo_de_Ana - 7 ) 

# Salida de datos
print(f"La edad de la abuela de Ana es: {edad_de_la_abuela_de_Ana_Actual}")