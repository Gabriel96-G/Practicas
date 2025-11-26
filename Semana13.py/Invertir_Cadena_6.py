def invertir_cadena(cadena):
    """
    Devuelve la cadena invertida usando recursión.
    """
    # Caso base: cadena vacía o de un solo carácter
    if len(cadena) <= 1:
        return cadena

    # Paso recursivo:
    # invertimos desde el segundo carácter en adelante
    # y luego agregamos el primero al final
    return invertir_cadena(cadena[1:]) + cadena[0]


def main():
    print("Programa para invertir una cadena (usando recursión)")
    texto = input("Introduce una palabra o frase: ")

    invertida = invertir_cadena(texto)

    print("Texto original :", texto)
    print("Texto invertido:", invertida)


if __name__ == "__main__":
    main()
