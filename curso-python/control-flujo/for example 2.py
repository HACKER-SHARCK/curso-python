# para desoues de encontrar los buscado en la base de datos el script se detenga
buscar = 3  # 10, 11, 4, 2.
for numero in range(5):  # range es un iterable
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
  # para imprimir si no la hubiera encontrado
else:
    print("no en contro el numero buscado")
