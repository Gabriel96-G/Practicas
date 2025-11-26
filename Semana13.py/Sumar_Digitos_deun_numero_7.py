def sumar_digitos(n):
    """
    Devuelve la suma de los dígitos de n usando recursión.
    """
    n = abs(n)  # por si el número es negativo

    # Caso base: si n tiene un solo dígito
    if n < 10:
        return n

    # Paso recursivo:
    # (último dígito) + (suma de los demás dígitos)
    ultimo = n % 10        # resto de dividir entre 10
    resto  = n // 10       # parte entera sin el último dígito
    return ultimo + sumar_digitos(resto)


def main():
    print("Programa: sumar los dígitos de un número (recursión)")
    numero = int(input("Introduce un número entero: "))
    resultado = sumar_digitos(numero)
    print(f"La suma de los dígitos de {numero} es {resultado}")


if __name__ == "__main__":
    main()
