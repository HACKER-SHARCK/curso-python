# def suma(a, b):
#   print(a + b)

# suma (2, 5)  #el resultado es 7

def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5, 7)
suma(2, 5)
suma(2, 8, 7, 45, 32)
