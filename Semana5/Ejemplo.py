'''
- Declaramos variables 
elementosFib=0,
listaFib=[0,1]
resultado=0 
- Vamos a pedirle al usuario el numero de elementos
de Fibonacci a imprimir
- Procedemos a hacer el càlculo de Fibonacci:
Si el usuario ingresa un numero negativo, damos un error
Si el usuario ingresa 0 la respuesta es 0
Si el usuario ingresa un 1, la respuesta es 1
Si el usuario ingresa un numero mayor o igual a 2, 
hacemos el calculo de Fibonacci sumando los dos elementos anteriores calculados
hasta llegar al elemento solicitado.
'''

# cantFib=0 # Esto se lo pedimos al usuario
# listaFib=[]
# resultado=0

# cantFib = int(input("Ingrese la cantidad de elementos de Fibonacci a mostrar: "))

# if cantFib >= 0:
#     for i in range(cantFib+1): # [0,1,2,3,4,5]
#         if i == 0 or i == 1:
#             listaFib.append(i)
#         else:
#             fib1 = listaFib[i-2] 
#             fib2 = listaFib[i-1]
#             resultado = fib1 + fib2
#             listaFib.append(resultado)
#     print(listaFib)
# else:
#     print("Debe ingresar un numero positivo o 0")


# N = int(input("Ingrese la cantidad de números de la serie Fibonacci: "))
# if N > 0:
#     a = 0
#     b = 1
#     print("Serie Fibonacci:")
#     for i in range(N+1):
#         print(a, end=" ")
#         a = b
#         b = a + b
# else:
#     print("Error: Debe ingresar un número positivo.")

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))