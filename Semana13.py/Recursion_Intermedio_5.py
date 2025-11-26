def maximo_lista(lista):
    """
    Devuelve el valor máximo de una lista usando recursión.
    """
    # Caso base: la lista no puede estar vacía
    if not lista:
        raise ValueError("La lista no puede estar vacía")

    # Caso base: cuando la lista tiene un solo elemento
    if len(lista) == 1:
        return lista[0]

    # Paso recursivo: calculamos el máximo del resto de la lista
    max_resto = maximo_lista(lista[1:])

    # Comparamos el primer elemento con el máximo del resto
    if lista[0] > max_resto:
        return lista[0]
    else:
        return max_resto


def main():
    print("Programa para encontrar el máximo de una lista (usando recursión)")
    numeros_str = input("Introduce números separados por espacios: ")

    # Convertimos la cadena en lista de enteros
    lista_numeros = [int(x) for x in numeros_str.split()]

    maximo = maximo_lista(lista_numeros)

    print("La lista es:", lista_numeros)
    print("El máximo es:", maximo)


if __name__ == "__main__":
    main()
