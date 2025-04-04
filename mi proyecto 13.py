import numpy as np

def bubble_sort(arr):
    """Función que ordena un arreglo usando el algoritmo Bubble Sort."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def ordenar_fila_matriz(matriz, fila):
    """Ordena una fila específica de la matriz en orden ascendente."""
    matriz[fila] = bubble_sort(matriz[fila].tolist())
    return matriz

# Crear una matriz 3x3 con valores aleatorios
matriz = np.random.randint(1, 100, (3, 3))

# Mostrar la matriz original
print("Matriz original:")
print(matriz)

# Fila a ordenar
fila_a_ordenar = 1  # Puedes cambiar este valor según la fila que quieras ordenar

# Ordenar la fila especificada
matriz_ordenada = ordenar_fila_matriz(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
print(matriz_ordenada)
