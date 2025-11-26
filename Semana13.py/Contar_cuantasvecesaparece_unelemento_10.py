def contar_apariciones(elem, lista):
    """
    Devuelve cuántas veces aparece elem en lista usando recursión.
    """
    # Caso base: lista vacía -> 0 apariciones
    if not lista:
        return 0

    # ¿El primer elemento es igual al que buscamos?
    cuenta_este = 1 if lista[0] == elem else 0

    # Paso recursivo: contar en el resto de la lista
    return cuenta_este + contar_apariciones(elem, lista[1:])


def main():
    print("Contar cuántas veces aparece un elemento en una lista (recursión)")
    
    numeros_str = input("Introduce números separados por espacios: ")
    lista_numeros = [int(x) for x in numeros_str.split()]

    elem = int(input("Introduce el número a contar: "))

    veces = contar_apariciones(elem, lista_numeros)

    print("Lista:", lista_numeros)
    print(f"El elemento {elem} aparece {veces} vez/veces.")


if __name__ == "__main__":
    main()
