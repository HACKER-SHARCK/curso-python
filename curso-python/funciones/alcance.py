saludo = 25


def saludar():
    global saludo  # NO UTILIZAR VARIABLES GLOBALES
    saludo = "Hola, mundo"


def saludaChanchito():
    saludo = 24
    print(saludo)


resultado1 = saludo + 3
print(resultado1)
saludar()
resultado2 = saludo + 3
print(resultado2)
