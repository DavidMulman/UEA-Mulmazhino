# Definir las dimensiones de la matriz
ciudades = ["Ciudad quito", "Ciudad loja", "Ciudad lago agrio"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4

# Crear la matriz 3D con valores de ejemplo (temperaturas)
temperaturas = [
    [[23, 24, 25, 26], [24, 25, 26, 27], [25, 26, 27, 28], [26, 27, 28, 29], [27, 28, 29, 30], [28, 29, 30, 31], [29, 30, 31, 32]],
    [[18, 19, 20, 21], [19, 20, 21, 22], [20, 21, 22, 23], [21, 22, 23, 24], [22, 23, 24, 25], [23, 24, 25, 26], [24, 25, 26, 27]],
    [[10, 11, 12, 13], [11, 12, 13, 14], [12, 13, 14, 15], [13, 14, 15, 16], [14, 15, 16, 17], [15, 16, 17, 18], [16, 17, 18, 19]]
]

# Calcular el promedio de temperaturas por ciudad y semana
promedios = []

for ciudad in range(len(ciudades)):
    promedios_ciudad = []
    for semana in range(semanas):
        suma_temperaturas = 0
        for dia in range(len(dias_semana)):
            suma_temperaturas += temperaturas[ciudad][dia][semana]
        promedio_semanal = suma_temperaturas / len(dias_semana)
        promedios_ciudad.append(promedio_semanal)
    promedios.append(promedios_ciudad)

# Mostrar el promedio de temperaturas para cada ciudad y semana
for ciudad in range(len(ciudades)):
    print(f"Promedios de temperatura para {ciudades[ciudad]}:")
    for semana in range(semanas):
        print(f"  Semana {semana + 1}: {promedios[ciudad][semana]:.2f} °C")
    print()
