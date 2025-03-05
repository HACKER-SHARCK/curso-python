usuarios = [
    ["chanchito", 4],
    ["felipe", 1],
    ["pulga", 5]
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)
# map
# nombres = [usuario[0] for usuario in usuarios]
# filtrar -filter
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]
# nombres = [usuario[0] for usuario in usuarios]
nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)
