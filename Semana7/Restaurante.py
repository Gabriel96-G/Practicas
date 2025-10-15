#Bienvenida#
print("===Bienvenido al sistema de Restaurante del Equipo 2===")

#Creacion del restaurante#
nombre_restaurante = input("Ingrese el nombre del restaurante: ")
print(f"Restaurante {nombre_restaurante} creado con exito ")

#Definir platillos, precio y disponibilida#
platillos = { 
    "1": {"nombre": "Hamburguesa", "precio": 5.000, "stock": 10},
    "2": {"nombre": "Pizza", "precio": 8.000, "stock": 5},
    "3": {"nombre": "Papas fritas", "precio": 3.000, "stock": 15}

}
#Lista donde guardamos las oredenes#
ordenes = []

while True:
    print("\n===menu===")
    print("1. Ver platillos")
    print("2. Crear una orden")
    print("3. Ver ordenes")
    print("4. Cambiar estado de orden")
    print("5. Finalizar una orden")
    print("6. Salir de la orden")

    opcion = input("Seleccione una opción: ")