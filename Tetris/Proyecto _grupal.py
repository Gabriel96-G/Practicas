Primera entrega 


while True:

    numero=input("Ingrese un numero:")

    if numero.isdigit():
        numero=int(numero)
        if numero < 20:
            print("El juego se encuntra en curso")
        elif numero == 20:
            print("Game Over")
            break
        else: 
            print("Dato no valido, intente ingresar otro dato") 
    else: 
        print("Dato no valido, intente ingresar otro dato")

