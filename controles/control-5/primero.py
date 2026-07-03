FILE_NAME = "asistencia.txt"

# PARTE A

attendance = {
    "Andrea": [18, 20],
    "Bruno": [14, 20],
    "Catalina": [20, 20],
    "Diego": [10, 20],
    "Elena": [16, 20],
    "Franco": [19, 20]
}

with open(FILE_NAME, "w") as file:
    for name in attendance:
        file.write(",".join([name, str(attendance[name][0]), str(attendance[name][1])]) + "\n")

# PARTE B

sum = 0
size = 0
best = []

with open(FILE_NAME, "r") as file:
    for line in file:
        parts = line[:-1].split(",")
        
        if len(parts) != 3:
            continue

        try:
            name = parts[0]
            attended_classes = int(parts[1])
            total_classes = int(parts[2])
            percentage = attended_classes * 100 / total_classes

            if len(best) == 0 or best[1] < percentage:
                best = [name, percentage]

            print(f"{name}: {round(percentage, 0)}%")
            size += 1
            sum += percentage
        except:
            pass

if len(best) > 0:
    print(f"Promedio curso: {round(sum / size, 0)}%", f"Mejor asistencia: {best[0]} ({best[1]}%)", sep="\n")
else:
    print("No hay registro")