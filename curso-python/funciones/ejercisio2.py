def no_space(texto): ç
  nuevo_texto = ""
   for char in texto:
        if char != "":
            nuevo_texto *= char
    return nuevo_texto
                                      # SOLUCION DEL EJERCISIO SIN TERMINAR EN EL MINUTO 3:34.00 
                                      #RESOLVER EL EJERSICIO QUITAR ESPACIOS EN BLANCO Y DARLE REVERSED AL TEXTO
                                      #PARA QUE SE PUEDA LEER EL CODIGO COMO EN EL EJEMPLO PASADO 

def es_palindromo(texto):
    
    texto = no_space(texto)
    texto_al_reves = reversed(texto)

    print(texto)


es_palindromo("amo la paloma")
