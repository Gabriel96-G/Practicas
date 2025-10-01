""" 
# Ejercicio 5: Validación de acceso

# Declaración de variables
usuario = ""
contrasena = ""
usuario_valido = "admin"
contrasena_valida = "1234"

# Entrada de datos
try:
    usuario = input("Ingrese el nombre de usuario: ")
    contrasena = input("Ingrese la contraseña: ")

    # Proceso
    if usuario == usuario_valido and contrasena == contrasena_valida:
        print("Acceso permitido")
    else:
        print("Acceso denegado")

except:
    print("Error en la entrada de datos")

"""

# Ejercicio 5: Validación de acceso
# Declaración de variables

usuario = ""
contrasena = ""
usuario_valido = "Majinboo"
contrasena_valida = "Chocolate"

# Entrada de datos
try:
    usuario = input("Ingrese el nombre de usuario: ")
    contrasena = input("Ingrese la contraseña: ")

    # Proceso
    if usuario == usuario_valido and contrasena == contrasena_valida:
        print("Acceso permitido")
    else:
        print("Acceso denegado")

except:
    print("Error en la entrada de datos")
