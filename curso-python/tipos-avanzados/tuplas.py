numeros = (1, 2, 3,) + (4, 5, 6)
print(numeros)

punto = tuple([1, 2])
print(punto)
menosnumeros = numeros[:2]
print(menosnumeros)
primero, segundo, *otros = numeros
print(primero, segundo, otros)
for n in numeros:
    print(n)

listanumeros = list(numeros)
listanumeros[0] = "chanchito feliz"
print(menosnumeros)
