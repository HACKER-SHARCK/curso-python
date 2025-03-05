numeros = [1, 2, 3]

# feo
# primero =numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

# MEJOR ASI
# primero, segundo, tercero = numeros
# print(primero, segundo, tercero)

# si necesitara solo el primer numero o objeto de lista
primero, *otros = numeros
print(primero)
# tambien puede ser
# primero, segundo, *otros = nuneros
# print(primero, segundo)
