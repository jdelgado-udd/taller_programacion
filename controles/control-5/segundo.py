FILE_NAME = "llegadas.txt"

# PARTE A

punctuality = {
    "Gabriela": "PUNTUAL",
    "Hernan": "ATRASADO",
    "Ignacia": "PUNTUAL",
    "Javier": "ATRASADO"
}

with open(FILE_NAME, "w") as file:
    for name in punctuality:
        file.write(",".join([name, punctuality[name]]) + "\n")

# PARTE B

added = {
    "Karen": "PUNTUAL",
    "Luis": "ATRASADO"
}

with open(FILE_NAME, "a") as file:
    for name in added:
        file.write(",".join([name, added[name]]) + "\n")

# PARTE C

def analizar_llegadas(filename):
    total = 0
    puntual = 0

    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line[:-1].split(",")
                
                if len(parts) != 2:
                    continue

                total += 1

                if parts[1] == "PUNTUAL":
                    puntual += 1
    except FileNotFoundError:
        print(f"Error: no se encontro el archivo {filename}")
        return
    
    print(f"Puntuales: {puntual}", f"Atrasados: {total - puntual}", sep="\n")

    if puntual < total - puntual:
        print("ALERTA: hay mas atrasados que puntuales")

analizar_llegadas(FILE_NAME)
analizar_llegadas("inexistente.txt")