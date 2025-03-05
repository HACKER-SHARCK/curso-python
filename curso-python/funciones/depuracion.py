def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado


# se le coloca un punto rojo (breakpoint) de retencion para que el depurador sepa donde detenerse
print("chanchito")
l = largo("hola, mundo")
print(l)
