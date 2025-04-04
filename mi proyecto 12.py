def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j
    return None

# Definir la matriz 3x3
matriz = [
    [5, 8, 2],
    [3, 7, 1],
    [6, 4, 9]
]

# Valor a buscar
valor_buscado = int(input("Ingrese el valor a buscar: "))

# Llamar a la función de búsqueda
resultado = buscar_valor(matriz, valor_buscado)

# Mostrar el resultado
if resultado:
    print(f"El valor {valor_buscado} se encuentra en la posición ({resultado[0]}, {resultado[1]})")
else:
    print(f"El valor {valor_buscado} no se encuentra en la matriz.")
