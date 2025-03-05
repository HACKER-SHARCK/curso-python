# si nuestra lista tiene longitud 4 el ultimo elemento viene siendo 3
mascotas = ["wolfgand", "pelusa", "pulga", "copito"]
print(mascotas[0])
# se modifica la primera opcion de la lista
mascotas[0] = "bicho"
print(mascotas)
# para pedir solo una fraccion de la lista
# si cambio el indice de la izquiera y lo dejo en [:3] python calculara que por defecto es 0 y la peticion empezara de 0
print(mascotas[0:3])
print(mascotas[-1])
