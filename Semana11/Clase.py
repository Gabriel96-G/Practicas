"""
Matrices en Python
""" 

m1 = [
    ['header1', 'header2', 'header3'],
    [1,1,1],
    [1,1,1],
    [1,1,1]
]

m2 = [
    ['kevin', 'test1', 31, 'admin'],
    ['Fulanito', 'test2', 20, 'user'],
    ['Menganito', 'test3', 25, 'user']
]

# # For each
# for fila in m2:
#     for columna in fila:
#         print(columna)

m3 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
m4 = [
    [2,4,6],
    [8,10,12],
    [14,16,18]
]

# Suma de matrices
resultado_suma = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

def suma_matrices(matriz1, matriz2):
    for i in range(len(matriz1)):
        for j in range(len(matriz1[i])):
            resultado_suma[i][j] = matriz1[i][j] + matriz2[i][j]
    return resultado_suma

print(suma_matrices(m3, m4))
