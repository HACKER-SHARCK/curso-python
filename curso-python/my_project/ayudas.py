"""CALCULADORA"""
# definimos una funcion llamada calcular que realizara las operaciones matematicas


def calcular():
    # imprimimos un mensaje incial
    print("calculadora simple")
    print("operaciones: +, -, *, /, ")
    try:  # usamos try-except para manejar errores si el usuario ingresa algo invalido
        # solicitamos el primer numero
        num1 = float(input("ingresa el primer numero: "))
        # pedimos al usuario que ingrese el operador matematico
        operador = input("ingresa la operacion:")
        # solicitamos el segundo numero y lo convertimos en tipo float
        num2 = float(input("ingresa el segundo numero:"))

        # comprobamos que operacion se quiere realizar y ejecutamos la correspondiente
        if operador == "+":  # si el operador es suma
            resultado = num1 + num2
        elif operador == "-":  # si el operador es resta
            resultado = num1 - num2
        elif operador == "*":  # si el operador es multiplicasion
            resultado = num1 * num2
        elif operador == "/":  # si el operador es division
            if num2 == 0:  # verificamos que el segundo numero no sea cero para evitar error
                print("Error no se puede dividir por cero.")
                return  # terminamos la ejecusion de la funcion si hay error
            resultado = num1 / num2
        else:  # si el operador ingresado no es valido
            print("operacion no valida.")
            return  # terminamos la ejecusion de la funcion
         # mostramos el resultado de la operacion
        print(f"resultado: {resultado}")
    except ValueError:  # si el usuario ingresa algo que no sea numero, mostramos un mensaje de error
        print("error ingresar numeros validos.")


     # llamamos a la funcion para que la calculdora se ejecute
calcular()
