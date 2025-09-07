# Definir dimensiones
ciudades = ["Otavalo", "Ibarra", "Tulcan"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 2  # Ejemplo con 2 semanas

# Crear matriz 3D con datos de ejemplo (ciudad x día x semana)
# Temperaturas inventadas
matriz_temperaturas = [
    [   # Ciudad 0: Otavalo
        [20, 21], [22, 23], [19, 20], [18, 19], [21, 22], [17, 18], [16, 17]
    ],
    [   # Ciudad 1: Ibarra
        [27, 29], [30, 31], [29, 28], [31, 30], [32, 33], [29, 30], [27, 28]
    ],
    [   # Ciudad 2: Tulcan
        [15, 16], [17, 18], [16, 15], [14, 15], [18, 19], [13, 14], [12, 13]
    ]
]

# Calcular promedios por ciudad y semana
for i in range(len(ciudades)):  # Recorrer ciudades
    for w in range(num_semanas):  # Recorrer semanas
        suma = 0
        for d in range(len(dias)):  # Recorrer días
            suma += matriz_temperaturas[i][d][w]
        promedio = suma / len(dias)
        print(f"Ciudad: {ciudades[i]}, Semana {w+1}, Promedio: {promedio:.2f} °C")