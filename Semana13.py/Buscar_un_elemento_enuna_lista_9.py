def buscar_elemento(elem, lista):
    """
    Devuelve True si elem está en lista, usando recursión.
    """
    # Caso base: lista vacía → no está
    if not lista:
        return False

    # Si el primer elemento es el que buscamos
    if lista[0] == elem:
        return True

    # Paso recursivo: buscar en el resto de la lista
    return buscar_elemento(elem, lista[1:])


def main():
    print("Programa para buscar un elemento en una lista (recursión)")

    # Pedimos la lista
    numeros_str = input("Introduce números separados por espacios: ")
    lista_numeros = [int(x) for x in numeros_str.split()]

    # Pedimos el elemento a buscar
    elem = int(input("Introduce el número a buscar: "))

    encontrado = buscar_elemento(elem, lista_numeros)

    print("Lista:", lista_numeros)
    if encontrado:
        print(f"El elemento {elem} SÍ está en la lista.")
    else:
        print(f"El elemento {elem} NO está en la lista.")


if __name__ == "__main__":
    main()
