def get_product(**datos):
    # se puede llegar solo al dato deseado con los parentesis cuadrado[] dentro de los parentesis
    print(datos["id"], datos["name"])


# el de la derecha es el diccionario
# el de la izquierda es el nombre del parametro
get_product(id="23",
            name="iphone",
            desc="esto es un iphone")
