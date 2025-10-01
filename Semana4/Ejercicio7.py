"""
Variables

Ingresar_calificacion

Si calificacion es mayor o igual a 90 y calificacion es igual o menor a 100 entonces
Letra = A
Si no calificacion es mayor o igual a 80 y calificacion es igual o mayor a 89 entonces
Letra = B
Si no calificacion es mayor o igual a 70 y calificacion es igual o mayor a 79 entonces
Letra = C
Si no calificacion es mayor o igual a 60 y calificacion es igual o mayor a 69 entonces
Letra = D
Si no calificacion es mayor o igual a 0 y calificacion es igual o mayor a 59 entonces
Letra = F
Si no imprima calificacion invalida

Letra por nota es, letra

"""
#Declarar variables

calificacion = float(input("ingrese calificacion"))

letra = ""
#Proceso
if calificacion >= 90 and calificacion <= 100:
    letra = "A"
elif calificacion >= 80 and calificacion <= 89:
    letra = "B"
elif calificacion >= 70 and calificacion <= 79:
    letra = "C"
elif calificacion >= 60 and calificacion <= 69:
    letra = "D"
elif calificacion >= 0 and calificacion <= 59:
    letra = "F"
else:
    print("Calificacion invalida")

#Salida de datos
if letra:
    print(f"Letra por nota es: {letra}")

