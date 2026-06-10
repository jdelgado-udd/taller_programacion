with open("puntajes.txt", "r") as archivo:  # abro y renombro con archivo
    lineas = archivo.readlines()

jugadores = {}  # hago un diccionario para guardar los datos uwu
mayorNombre = ""  # como desconozco al mayor, queda vacio

for linea in lineas:
    lineaStrip = linea.strip("\n")  # sacar \n
    lineaSplit = lineaStrip.split(",")  # los separo en las , de cada cosito uwu

    nombre = lineaSplit[0]  # Pongo el nombre en una variable
    puntaje = int(
        lineaSplit[1]
    )  # Pongo el puntaje en una variable y lo transformo a entero

    jugadores[nombre] = puntaje  # guardo nombre y puntaje en el diccionario jugadores

    if (
        mayorNombre == "" or jugadores[mayorNombre] < puntaje
    ):  # Veo si el mayor es vacio, si lo es, le coloco el primer nombre
        mayorNombre = nombre

prom = sum(jugadores.values()) / len(jugadores)

print("el putaje promedio es:", prom)
print("el puntaje mayor es", jugadores[mayorNombre], "y es de", mayorNombre)
