"""
Principio de Responsabilidad Unica -> Atomicidad del codigo
Debemos Procurar que nuestras funciones estèn suficientemente dividas como para que
resuelvan solo un problema o una parte del problema
"""

def saludar():
    print("Hola")

def sumar(numero1, numero2):
    return numero1 + numero2

saludo = saludar()
print(saludo)
num1 = int(input("Ingrese num1: "))
num2 = int(input("Ingrese num2: "))
resultado = sumar(num1, num2)
resultado = sumar(2,6)
print(f"resultado: {resultado}")



**********************************************************************************


# """
# Principio de Responsabilidad Unica -> Atomicidad del codigo
# Debemos Procurar que nuestras funciones estèn suficientemente dividas como para que
# resuelvan solo un problema o una parte del problema
# """

# def saludar():
#     print("Hola")

# def sumar(numero1, numero2):
#     return numero1 + numero2

# saludo = saludar()
# print(saludo)
# num1 = int(input("Ingrese num1: "))
# num2 = int(input("Ingrese num2: "))
# resultado = sumar(num1, num2)
# resultado = sumar(2,6)
# print(f"resultado: {resultado}")

def sumar(numero1, numero2):
     return numero1 + numero2

def restar(numero1, numero2):
    return numero1 - numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

def dividir(numero1, numero2):
    if numero2 == 0:
        return False
    return numero1 / numero2

def solicitar_numeros():
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    return num1, num2

def menu():
    print("*"*20)
    print("Bienvenido a mi Calculadora\n")
    print("Ingrese una de las opciones para operaciones: ")
    print("1. Sumar\n" \
          "2. Restar\n" \
          "3. Dividir\n" \
          "4. Multiplicar\n" \
          "0. Salir")
    print("*"*20)

def main():
    menu()
    opcion = int(input("Ingrese una de las opciones: "))
    while opcion != 0:
        if opcion == 1:
            num1, num2 = solicitar_numeros()
            resultado = sumar(num1, num2)
            print(f"El resultado de la suma es: {resultado}")
        elif opcion == 2:
            num1, num2 = solicitar_numeros()
            resultado = restar(num1, num2)
            print(f"El resultado de la resta es: {resultado}")
        elif opcion == 3:
            num1, num2 = solicitar_numeros()
            resultado = dividir(num1, num2)
            if resultado == False:
                print("No se puede dividir por 0")
            else:
                print(f"El resultado de la division es: {resultado}")
        elif opcion == 4:
            num1, num2 = solicitar_numeros()
            resultado = multiplicar(num1, num2)
            print(f"El resultado de la multiplicacion es: {resultado}")
        else:
            print("Opcion invalida, vuelva a intentarlo")
        menu()
        opcion = int(input("Ingrese una de las opciones: "))
    print("Adios!!")

main()