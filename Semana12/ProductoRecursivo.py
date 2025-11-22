""" 
3. Producto Recursivo
Implementar multiplicación de dos números usando solo sumas recursivas.

"""
def producto_recursivo(a, b):
    # Caso base: si b es 0, el producto es 0
    if b == 0:
        return 0
    # Caso recursivo: a * b = a + a * (b - 1)
    return a + producto_recursivo(a, b - 1)

def main():
    entrada_a = input("Ingrese el primer número (a): ")
    entrada_b = input("Ingrese el segundo número (b, entero no negativo): ")
    try:
        a = float(entrada_a)
        b = int(entrada_b)
        if b < 0:
            print("El segundo número debe ser un entero no negativo.")
            return
        resultado = producto_recursivo(a, b)
        print(f"El producto de {a} y {b} es: {resultado}")
    except ValueError:
        print("Entrada no válida. Asegúrese de ingresar un número para el primer valor y un entero no negativo para el segundo.")
if __name__ == "__main__":
    main()

