# los diccionarios son muy importantes en python porque son como bases de datos

punto = {"X": 25, "y": 50}
print(punto)
print(punto["X"])
print(punto["y"])

punto["z"] = 45
# print(punto, punto["lala"])
if "lala" in punto:
    print("encontre lala", punto["lala"])

# funcion get
print(punto.get("x"))
print(punto.get("lala", 97))

# funcion del permite eliminar
del punto["X"]
del (punto["y"])

print(punto)
punto["X"] = 25

# iterar llaves dentro de python por su valor con (For)
for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

# un uso realista de los diccionrios en python

usuarios = [
    {"id": 1, "nombre": "chanchito"},
    {"id": 2, "nombre": "feliz"},
    {"id": 3, "nombre": "nicolas"},
    {"id": 4, "nombre": "felipe"},
]

for usuario in usuarios:
    print(usuario["nombre"])
