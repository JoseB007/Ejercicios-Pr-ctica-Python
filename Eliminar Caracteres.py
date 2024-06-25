#  * Crea una función que reciba dos cadenas como parámetro (str1, str2)
#  * e imprima otras dos cadenas como salida (out1, out2).
#  * - out1 contendrá todos los caracteres presentes en la str1 pero NO
#  *   estén presentes en str2.
#  * - out2 contendrá todos los caracteres presentes en la str2 pero NO
#  *   estén presentes en str1.

def eliminarCaracteres(str1, str2):
    out1 = ""
    out2 = ""
    for i in str1:
        if i not in str2:
            out1 += i

    for j in str2:
        if j not in str1:
            out2 += j
    
    return out1, out2


str1 = "abcdefa"
str2 = "bdfhij"

print(eliminarCaracteres(str1, str2))


def caracteresUnicos(str1, str2):
    set_str1 = set(str1)
    set_str2 = set(str2)

    uno = set_str1 - set_str2
    dos = set_str2 - set_str1

    out1 = ''.join(uno)
    out2 = ''.join(dos)

    return out1, out2

print(caracteresUnicos(str1, str2))