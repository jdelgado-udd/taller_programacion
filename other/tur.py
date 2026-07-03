def validarrut(rut):
    i = 2
    x = rut.replace(".", "")
    tur = list(reversed(x.split("-")))
    verificador = tur[0]
    numeros = tur[1]
    suma = 0

    for numero in numeros[::-1]:
        suma += int(numero) * i
        i += 1
        if i == 8:
            i = 2

    resto = 11 - (suma % 11)

    if resto == 11:
        control = "0"
    elif resto == 10:
        control = "k"
    else:
        control = str(resto)

    return verificador.lower() == control.lower()

print(validarrut("22.682.074-4"))