# DICCIONARIOS
#
# Que es:
# llaves = []
# valores = []
#
# diccionario[x] = y
# x una llave
# y un valor
#
# Como creo uno:
# diccionario = {}
#
# Como me manejo con uno:
# diccionario[llave] = valor
# variableQueTieneElValor = diccionario[llave]
#
# diccionario.keys() -> lista que tiene todas las llaves
# diccionario.values() -> lista que tiene todos los valores

supermercado = {"peras": 3}

supermercado["manzanas"] = 2

valorDeManzanas = supermercado["manzanas"]

if supermercado["peras"] == 3:
    print("Hay 3 peras, llegamos al máximo")

print(supermercado.keys())
print(supermercado.values())

producto = "manzanas"

print(supermercado["manzanas"] == supermercado[producto])
