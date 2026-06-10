registros = [
    ["Ana Reyes", 312.0],
    ["Carlos Muñoz", 874.5],
    ["Ana Reyes", 480.0],
    ["Luis Vera", 156.0],
    ["Carlos Muñoz", 543.0],
    ["Luis Vera", 820.0],
    ["Ana Reyes", 695.0]
]

flota = {
    "empresa": "TransAndes Ltda.",
    "turno": "nocturno",
    "velocidad_limite": 85
}

# Code start

viajes = []

for registro in registros:
    index = -1

    for i in range(len(viajes)):
        viaje = viajes[i]
        if viaje[0] == registro[0]:
            index = i
            break
    
    if index == -1:
        viajes.append([registro[0], [registro[1]]])
    else:
        viajes[index][1].append(registro[1])

print(viajes)

for viaje in viajes:
    print(
        f"{viaje[0]}:",
        f" #{len(viaje[1])} viajes",
        f" {round(sum(viaje[1]), 1)}km recorridos",
        f" {round(sum(viaje[1]) / len(viaje[1]), 1)}km en promedio",
        f" {round(max(viaje[1]), 1)}km en viaje más largo",
        sep="\n"
    )

conductor = input("Ingrese el nombre de un conductor: ")
distancia = input("Ingrese una distancia en km: ")

try:
    distancia = float(distancia)
except ValueError:
    print("Distancia inválida")
    quit()

agregado = False

for viaje in viajes:
    if viaje[0] == conductor:
        agregado = True
        viaje[1].append(distancia)
        print("Conductor actualizado!")
        print("Historial de conductor: " + str(viaje[1]))
        break

if not agregado:
    viajes.append([conductor, [distancia]])
    print("Conductor agregado!")
    print("Historial de conductor: " + str([distancia]))

print(flota["empresa"].upper() + " | " + flota["turno"].upper())