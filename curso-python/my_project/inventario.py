# Diccionario que almacena los productos y su cantidad en el inventario
inventario = {
    "Manzana": 50,
    "Banana": 100,
    "Leche": 30,
    "Pan": 40
}

# Bucle principal que permite interactuar con el programa
while True:
    # Muestra el inventario actual
    print("\nInventario actual:")
    # Recorre el inventario y muestra cada producto con su cantidad
    for producto, cantidad in inventario.items():
        print(f"{producto}: {cantidad}")

    # Muestra las opciones disponibles para el usuario
    print("\nOpciones:")
    print("1. Agregar productos")  # Opción para agregar productos
    print("2. Eliminar productos")  # Opción para eliminar productos
    print("3. Salir")  # Opción para salir del programa
    # Solicita al usuario elegir una opción
    opcion = input("Elige una opción: ")

    # Si elige la opción 1 (agregar productos)
    if opcion == '1':
        # Solicita al usuario el nombre del producto a agregar
        producto = input("Ingresa el nombre del producto a agregar: ")
        # Solicita la cantidad del producto que desea agregar
        cantidad = int(input(f"¿Cuántos {producto}s deseas agregar? "))
        # Verifica si el producto ya existe en el inventario
        if producto in inventario:
            # Si existe, se aumenta la cantidad del producto
            inventario[producto] += cantidad
        else:
            # Si no existe, se agrega el producto con la cantidad especificada
            inventario[producto] = cantidad
        # Muestra un mensaje confirmando que el producto fue agregado
        print(f"Se han agregado {cantidad} {producto}s.")

    # Si elige la opción 2 (eliminar productos)
    elif opcion == '2':
        # Solicita el nombre del producto a eliminar
        producto = input("Ingresa el nombre del producto a eliminar: ")
        # Verifica si el producto existe en el inventario
        if producto in inventario:
            # Solicita la cantidad de producto que desea eliminar
            cantidad = int(input(f"¿Cuántos {producto}s deseas eliminar? "))
            # Verifica si hay suficiente cantidad para eliminar
            if inventario[producto] >= cantidad:
                # Si hay suficiente, se elimina la cantidad especificada
                inventario[producto] -= cantidad
                print(f"Se han eliminado {cantidad} {producto}s.")
            else:
                # Si no hay suficiente cantidad, muestra un mensaje de error
                print(f"No hay suficientes {producto}s en inventario.")
        else:
            # Si el producto no se encuentra en el inventario, muestra un mensaje de error
            print("Producto no encontrado.")

    # Si elige la opción 3 (salir)
    elif opcion == '3':
        # Muestra un mensaje de despedida y sale del bucle
        print("Saliendo del programa.")
        break  # Sale del bucle y termina el programa

    # Si elige una opción no válida
    else:
        # Muestra un mensaje de error por elegir una opción no válida
        print("Opción no válida.")
