matriz = [
[13, 99, 1],
[67, 3, 0],
[23, 78, 34]
]

def ordenar_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[fila][j] > matriz[fila][j+1]:
# CAMBIAR ELEMENTOS
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]
    return matriz

# MATRIZ
print("Matriz original:")
for fila in matriz:
    print(fila)


# ESCOJER LA FILA A ORDENAR
fila_a_ordenar = 2
matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)


# MUESTRA LA MATRIZ ORDENADA
print(f"\nMatriz después de ordenar la fila {fila_a_ordenar}:")
for fila in matriz_ordenada:
    print(fila)