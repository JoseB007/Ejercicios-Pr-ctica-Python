#  * Crea una función que reciba un String de cualquier tipo y se encargue de
#  * poner en mayúscula la primera letra de cada palabra.
#  * - No se pueden utilizar operaciones del lenguaje que
#  *   lo resuelvan directamente.



def convertirMayuscula(texto):
    texto = texto.split(' ')
    textoCapitalize = ""
    for palabra in texto:
        textoCapitalize +=  palabra.capitalize() + " "

    return textoCapitalize


texto = 'el coronel no tiene quien le escriba'
print(convertirMayuscula(texto))