def moda(numeros: list[float]) -> list[float]:
    if len(numeros) == 0:
        return []

    diccionario: dict[float, int] = {}
    maximos: list[float] = [numeros[0]]

    for numero in numeros:
        if numero in diccionario:
            diccionario[numero] += 1
        else:
            diccionario[numero] = 1

        if diccionario[maximos[0]] == diccionario[numero] and numero not in maximos:
            maximos.append(numero)

        if diccionario[maximos[0]] < diccionario[numero]:
            maximos = [numero]

    return sorted(maximos)