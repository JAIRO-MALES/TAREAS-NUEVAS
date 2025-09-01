# Programa de busqueda de datos en matriz 3x3

matriz_tarea = [
[2, 23, 15],
[13, 4, 45],
[57, 9, 17]
]

def buscar_valor(matriz_tarea, valor):
    for i in range(len(matriz_tarea)):
        for j in range(len(matriz_tarea[i])):
            if matriz_tarea[i][j] == valor:
                return (i, j)
    return None
#AQUI COLOCAMOS EL VALOS A BUSCAR EN LA MATRIZ
valor_abuscar = 13
resultado = buscar_valor(matriz_tarea, valor_abuscar)

# MUESTRA LOS RESULTADOS
if resultado:
    print(f"El valor {valor_abuscar} se encontró en la posición: fila {resultado[0]}, columna {resultado[1]}")
else:
    print(f"El valor {valor_abuscar} no se encontró en la matriz.")