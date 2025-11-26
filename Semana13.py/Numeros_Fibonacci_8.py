def fibonacci(n):
    """
    Devuelve el n-ésimo número de Fibonacci usando recursión.
    F(0) = 0, F(1) = 1
    """
    if n < 0:
        raise ValueError("n debe ser un entero mayor o igual a 0")

    # Casos base
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Paso recursivo
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    print("Programa para calcular el n-ésimo número de Fibonacci (recursivo)")
    n = int(input("Introduce un número entero n (>= 0): "))

    resultado = fibonacci(n)

    print(f"Fibonacci({n}) = {resultado}")


if __name__ == "__main__":
    main()
