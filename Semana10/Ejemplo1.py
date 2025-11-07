import pprint
# with open("./Semana10/numeros.txt", "r") as file:  # r -> solo lectura, w -> escritura, a -> append (agregar al final del archivo)
#     for line in file:
#         numero = int(line.strip())   # strip -> Elimina los trailing blank spaces y \n y el int() lo conviert a entero
#         print(numero**2)
#     file.close()

with open("./Semana10/usuarios.csv", "r") as file:
    lista_usuarios = []
    for line in file:
        usuario = {}
        nueva_linea = line.strip()
        nueva_linea = nueva_linea.split(",")   # split -> Separa la cadena de texto en una lista de elementos, por defecto separa por comas
        usuario["nombre"] = nueva_linea[0]
        usuario["apellido"] = nueva_linea[1]
        usuario["edad"] = nueva_linea[2]
        usuario["ocupacion"] = nueva_linea[3]
        lista_usuarios.append(usuario)
    file.close()
pprint.pprint(lista_usuarios)

usuario_nuevo = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 30,
    "ocupacion": "Ingeniero"
}

lista_usuarios.append(usuario_nuevo)

with open("./Semana10/usuarios.csv", "w") as file:
    file.write(str(lista_usuarios))
    file.close()

pprint.pprint(lista_usuarios)