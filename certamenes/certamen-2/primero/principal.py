import transporte

# Python en este PC me estaba dando un mal rato con los caminos,
# opté por pegar el camino entero, por favor reemplazar con "" en
# un entorno de Python bien configurado.
datos_path = ""
camiones = {}

with open(f"{datos_path}/datos.csv", "r") as file:
    lines = file.readlines()
    columns = lines[0].strip("\n").split(",")

    for i in range(1, len(lines)):
        line = lines[i].strip("\n").split(",")
        data = {}

        for j in range(1, len(line)):
            if j == 1:
                data[columns[j]] = line[j]
                continue

            try:
                data[columns[j]] = float(line[j])
            except ValueError:
                print(f"Failed to include numeric value from column {j} in line {i}.")
                data[columns[j]] = 0

        camiones[line[0]] = data

camiones_riesgo = {}

for patente, camion in camiones.items():
    camion_eficiencia = transporte.eficiencia(
        camion["distancia_km"], camion["combustible_litros"]
    )
    camion_velocidad_prom = transporte.velocidad_promedio(
        camion["distancia_km"], camion["tiempo_horas"]
    )
    camion_carga_rel = transporte.carga_relativa(camion["peso_carga_ton"])

    riesgo = 0

    if camion_eficiencia > 35 / 100:
        riesgo += 2

    if camion_velocidad_prom > 90:
        riesgo += 3

    if camion_carga_rel > 95:
        riesgo += 1

    if riesgo >= 4:
        camiones_riesgo[patente] = riesgo

with open(f"{datos_path}/camiones_riesgo.csv", "w") as file:
    file.write("patente,conductor,puntaje_riesgo\n")

    for patente, riesgo in camiones_riesgo.items():
        conductor = camiones[patente]["conductor"]
        file.write(f"{patente},{conductor},{riesgo}\n")
