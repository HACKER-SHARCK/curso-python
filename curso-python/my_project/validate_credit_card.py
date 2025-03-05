# solicita al usuario que ingrese el numero e tarjeta de credito
tarjeta = input("ingrese el numero de la tarjeta de credito ")

# convierte cada digito de la cadena de entrada en un entero y lo almacena en una lista llamada "digitos"
digitos = [int(d) for d in tarjeta]
# recorre los digitos de la tarjeta de credito comenzando desde el segundo digitomenos significativo hasta el primer digito
# con un paso de 2
for i in range(len(digitos)-2, -1, -2):
 # duplica el valor del digito en la posicion actual
    digitos[i] *= 2
 # si el resultado de la muktiplicasion es mayor que 9, resta 9 al resultado
    if digitos[i] > 9:
        digitos[i] -= 9
 # calcula suma de todos los digitos de la lista "digitos" despues de duplicar  las modificasiones
suma = sum(digitos)
# esto indica que la tarjeta de credito es valida segun el algoritmo de luhn
# imorime true si es valudo, false en caso contrario
print(suma % 10 == 0)
