file = open("../../data/items.txt", "r+")
lines = file.readlines()

for index in range(len(lines)):
    parts = lines[index].split(",")

    if parts[-1] == "0":
        parts[-1] = "sin stock"
        lines[index] = ",".join(parts)

file.seek(0, 0)
file.writelines(lines)
file.close()
