def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j  # Retorna la posición (fila, columna)
    return None  # Retorna None si no se encuentra el valor


# Definir la matriz
matriz = [
    [5, 8, 3],
    [4, 7, 1],
    [9, 6, 2]
]

# Pedir un valor al usuario
valor_a_buscar = int(input("Ingrese el valor a buscar en la matriz: "))

# Buscar el valor
posicion = buscar_valor(matriz, valor_a_buscar)

# Mostrar el resultado
if posicion:
    print(f"El valor {valor_a_buscar} se encuentra en la posición {posicion}")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz")
