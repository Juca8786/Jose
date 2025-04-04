import random

# Definir las dimensiones de la matriz
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2  # Número de semanas

# Generar una matriz 3D con temperaturas aleatorias entre 10 y 30 grados
temperaturas = [[[random.randint(10, 30) for _ in dias_semana] for _ in range(semanas)] for _ in ciudades]

# Calcular el promedio de temperaturas para cada ciudad por semana
for i, ciudad in enumerate(ciudades):
    print(f"\nPromedio de temperaturas en {ciudad}:")
    for semana in range(semanas):
        promedio = sum(temperaturas[i][semana]) / len(dias_semana)
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")
