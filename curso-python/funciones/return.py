def suma(a, b):

    resultado = a + b

    return resultado  # el return me deja utilizar el resultado de la operacion mas adelante


c = suma(1, 2)  # en "c" se guarda el resultado de la primera operacion
# se suma el resultado de la priomera operacion guardado en c y los suma con el siguiente numero
d = suma(c, 2)

print(d)
