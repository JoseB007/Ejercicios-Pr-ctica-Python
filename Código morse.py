#  * Crea un programa que sea capaz de transformar texto natural a código
#  * morse y viceversa.
#  * - Debe detectar automáticamente de qué tipo se trata y realizar
#  *   la conversión.
#  * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
#  *   o símbolos y dos espacios entre palabras "  ".
#  * - El alfabeto morse soportado será el mostrado en

dicc_codigo_morse = {
    'a': '.-',
    'b': '-..',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..'
}

def convertirMorseTexto(cadena):
    cadena.lower()
    cod_morse = ""
    
    for letra in cadena:
        if letra in dicc_codigo_morse:
            cod_morse += dicc_codigo_morse[letra]

    cadena_morse = cod_morse[::1]

    return cadena_morse
cadena = 'hola'
print(convertirMorseTexto(cadena))