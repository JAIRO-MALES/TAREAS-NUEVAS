def calcular_promedio_ciudades(ciudades, dias, num_semanas, matriz_temperaturas):
    resultados = {}

    for i in range(len(ciudades)):  # recorrer ciudades
        resultados[ciudades[i]] = []  # lista de promedios de esa ciudad
        for w in range(num_semanas):  # recorrer semanas
            suma = 0
            for d in range(len(dias)):  # recorrer días
                suma += matriz_temperaturas[i][d][w]
            promedio = suma / len(dias)
            resultados[ciudades[i]].append(promedio)

    return resultados

ciudades = ["Otavalo", "Ibarra", "Tulcán"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 2

matriz_temperaturas = [
    [[20, 21], [22, 23], [19, 20], [18, 19], [21, 22], [17, 18], [16, 17]],  # Otavalo
    [[27, 29], [30, 31], [29, 28], [31, 30], [32, 33], [29, 30], [27, 28]],  # Ibarra
    [[15, 16], [17, 18], [16, 15], [14, 15], [18, 19], [13, 14], [12, 13]]  # Tulcán
]

resultados = calcular_promedio_ciudades(ciudades, dias, num_semanas, matriz_temperaturas)

# Mostrar resultados
for ciudad, promedios in resultados.items():
    for semana, valor in enumerate(promedios, start=1):
        print(f"Ciudad: {ciudad}, Semana {semana}, Promedio: {valor:.2f} °C")
