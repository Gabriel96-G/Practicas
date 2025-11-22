"""
4. Contar Digitos
Dado un número entero, retornar cuantos digitos tiene usando recursión.
12345 -> 5
213 -> 3
1000000 -> 7

"""

def contar_digitos(n):
    # Caso base: si n es menor que 10, tiene 1 dígito
    if n < 10:
        return 1
    # Caso recursivo: eliminar el último dígito y contar el resto
    return 1 + contar_digitos(n // 10)

def main():
    entrada = input("Ingrese un número entero positivo para contar sus dígitos: ")
    try:
        n = int(entrada)
        if n < 0:
            print("Por favor, ingrese un número entero positivo.")
            return
        cantidad_digitos = contar_digitos(n)
        print(f"El número {n} tiene {cantidad_digitos} dígitos.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero positivo.")

if __name__ == "__main__":
    main()

