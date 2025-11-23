def estado_juego():
    while True:
        dato = input("\nIngrese el apilamiento (0 a 20): ")
        try:
            apilamiento = int(dato)
            if apilamiento < 0 or apilamiento > 20:
                print("\nOpción inválida!!! \nPor favor ingrese un numero entero entre 0 y 20. ")
            else:
                if apilamiento < 20:
                    print("\nJuego en curso.")
                else:
                    print("\nGAME OVER")
                break
        except ValueError:
            print("\nOpción inválida!!! \nPor favor ingrese un numero entero entre 0 y 20. ")

def puntaje_acumulado():
    while True:
        dato = input("\nIngrese cantidad de lineas (0 a 50): ")
        try:
            N = int(dato)
            if N < 0 or N > 50:
                print("\nOpción inválida!!! \nPor favor ingrese un numero entero entre 0 y 50.")
            else:
                fN= (5 * N * (N + 1)) // 2
                print("Su puntaje acumulado es de =", fN, "pts.")
                break
        except ValueError:
            print("\nOpción inválida!!! \nPor favor ingrese un numero entero entre 0 y 50.")

def piezas_tetris():

    piezas = {
        "o": "****\n*  *\n*  *\n****",
        "l": "*\n*\n*\n*",
        "s": " **\n** ",
        "z": "** \n **",
        "L": "*  \n*  \n** ",
        "J": "  *\n  *\n **",
        "T": "*****\n  * \n  * "
    }

    while True:
        ch = input("\nIngrese la letra de la pieza \n(o, l, s, z, L, J, T): ")

        if len(ch) != 1:
            print("\nDebe de ingresar un solo carácter ")
            continue
        if ch in piezas:
            print(piezas[ch])
            break
        else:
            print("\nOpción inválida!!! \nPor favor ingrese un carácter valido.")

def orientacion_final():
    while True: 
        orientacion = input("\nIngrese orientación inicial \n(A, a, d, i): ")

        orientaciones =['A', 'd', 'a', 'i']

        if orientacion not in orientaciones:
            print("\nOpción inválida!!! \nPor favor ingresar una orientación válida (A, a, d, i).")
            continue

        try:
            rot_d = int(input("Ingrese cantidad de rotaciones a la derecha: "))
            rot_i = int(input("Ingrese cantidad de rotaciones a la izquierda: "))

            if rot_d < 0 or rot_i < 0:
                print("\nOpción inválida!!! \nLas rotaciones deben ser números enteros positivos.")
                continue

            total = (rot_d - rot_i) % 4

            pos = orientaciones.index(orientacion)
            nueva_pos = (pos + total) % 4
            pos_final = orientaciones[nueva_pos]

            print("\nLa orientacion final de la pieza es:", pos_final)
            break
        except ValueError:
            print("\nOpción inválida!!! \nLas rotaciones deben ser números enteros positivos.")

def menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Estado del juego")
    print("2. Puntaje acumulado")
    print("3. Piezas de Tetris")
    print("4. Orientacion final de la pieza")
    print("0. Salir")

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        estado_juego()
    elif opcion == "2":
        puntaje_acumulado()
    elif opcion == "3":
        piezas_tetris()
    elif opcion == "4":
        orientacion_final()
    elif opcion == "0":
        print("\n===Juego finalizado=== \nGracias por jugar!!!  \nSaliendo del programa... ")        
        break
    else:
        print("\nOpción inválida \nIntente nuevamente")