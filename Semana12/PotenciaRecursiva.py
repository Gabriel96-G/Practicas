""" 
2. Potencia Recursiva
Implementar una función que calcule a^b usando recursión.

"""

def potencia_recursiva(a, b):
    # Caso base: cualquier número elevado a la potencia 0 es 1
    if b == 0:
        return 1
    # Caso recursivo: a^b = a * a^(b-1)
    return a * potencia_recursiva(a, b - 1)

def main():
    entrada_a = input("Ingrese la base (a): ")
    entrada_b = input("Ingrese el exponente (b, entero no negativo): ")
    try:
        a = float(entrada_a)
        b = int(entrada_b)
        if b < 0:
            print("El exponente debe ser un entero no negativo.")
            return
        resultado = potencia_recursiva(a, b)
        print(f"{a} elevado a la potencia {b} es: {resultado}")
    except ValueError:
        print("Entrada no válida. Asegúrese de ingresar un número para la base y un entero no negativo para el exponente.")

if __name__ == "__main__":
    main()

