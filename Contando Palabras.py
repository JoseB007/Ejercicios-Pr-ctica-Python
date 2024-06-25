#  * Crea un programa que cuente cuantas veces se repite cada palabra
#  * y que muestre el recuento final de todas ellas.
#  * - Los signos de puntuación no forman parte de la palabra.
#  * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#  * - No se pueden utilizar funciones propias del lenguaje que
#  *   lo resuelvan automáticamente.


def contadorPalabras(texto):
    texto = texto.lower()
    palabras = texto.split(' ')
    conteo_palabras = {}

    for palabra in palabras:
        if palabra in conteo_palabras:
            conteo_palabras[palabra] += 1
        else:
            conteo_palabras[palabra] = 1

    return conteo_palabras

texto = "Hola, hola! ¿Cómo estás? Hola, estoy bien. ¿Y tú?"
print(contadorPalabras(texto))