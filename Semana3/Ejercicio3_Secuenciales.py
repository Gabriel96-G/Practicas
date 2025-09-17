

# Variables
peso = 0.0
altura = 0.0
imc = 0.0
nombre = ""


# Entrada de datos
nombre = input("Ingrese su nombre: ")
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

# Operaciones
imc = peso / (altura ** 2)


# Salida de datos
print(f"Hola {nombre}!, su IMC es de : {imc}")
print(f"Hola {nombre}!, su IMC es de : {imc:.2f}")


print("Hola  " + nombre + "!, su IMC es de : " + str(imc))


print(f"Hola {nombre}!, su IMC es de: {imc:.2f}")
print("Hola " + nombre + "!, su IMC es de: " + str(imc) + "!")
print("Hola " + nombre + "!, su IMC es de: " + str(round(imc, 2)) + "!")