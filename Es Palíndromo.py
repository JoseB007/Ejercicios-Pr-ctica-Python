#  * Escribe una función que reciba un texto y retorne verdadero o
#  * falso (Boolean) según sean o no palíndromos.
#  * Un Palíndromo es una palabra o expresión que es igual si se lee
#   * de izquierda a derecha que de derecha a izquierda.
#  * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
#  * Ejemplo: Ana lleva al oso la avellana.

def esPalindromo(cadena):
    cadena = cadena.lower()
    cadena_original = ""
    for i in cadena:
        if i != ' ':
            cadena_original += i
    
    cadena_invertida = ""
    for j in range(len(cadena_original)-1, -1, -1):
        cadena_invertida += cadena_original[j]

    if cadena_original == cadena_invertida:
        return True
    else:
        return False

    # return cadena_invertida, cadena_original

str1 = 'Sé verlas al revés'
print(esPalindromo(str1))

str2 = 'Sé verlas al revéz'
print(esPalindromo(str2))