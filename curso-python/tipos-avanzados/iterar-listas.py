mascotas = ["pelusa", "pulga", "felipe", "chanchito feliz"]
# la funcion enumerate lo que hace es que le tira toda la lista de la variable mascotas enumeradas
primero, segundo = [1, 2]
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
