# En el taller de Santa 🎅, algunos mensajes navideños han sido escritos de manera peculiar: las letras dentro de los paréntesis deben ser leídas al revés

# Santa necesita que estos mensajes estén correctamente formateados. Tu tarea es escribir una función que tome una cadena de texto y revierta los caracteres dentro de cada par de paréntesis, eliminando los paréntesis en el mensaje final.

# Eso sí, ten en cuenta que pueden existir paréntesis anidados, por lo que debes invertir los caracteres en el orden correcto.


# a = 'odnum'

# def decode(mensaje):
#     c = ""
#     for i in range(len(mensaje)-1, -1, -1):
#         c+=(mensaje[i])
    
#     return c

# print(decode(a))


# def reversion(cadena):
#     lista_parentesis = cadena.split()
#     palabras_sinParentesis = []
#     p = ""
#     nueva_cadena = ""
#     for parentesis in lista_parentesis:
#         if '(' in parentesis:
#             for c in range((len(parentesis)-1)-1, 0, -1):
#                 p += parentesis[c]
#             palabras_sinParentesis.append(p)
#             p = ""
#         else:
#             palabras_sinParentesis.append(parentesis)

#     nueva_cadena = (' ').join(palabras_sinParentesis)

#     return nueva_cadena

# print(reversion(cadena))



cadena4 = "hola (odnum (feliz))"
cadena3 = "sa(u(cla)atn)s"
cadena2 = "(olleh) (dlrow)!"
cadena1 = "hola (odnum)"

def n_reversion(cadena):
    cadena_parentesis = ""
    cadena_invertida = ""
    cadena_resultado = ""
    ini = 0
    fin = 0

    for i in range(len(cadena)):
        if cadena[i] == '(':
            ini = i
        if cadena[i] == ')':
            fin = i
            break
        
    for l in range(ini, fin+1, 1):
        cadena_parentesis += cadena[l]

    cadena_invertida += cadena_parentesis[-2:0:-1]
    cadena_resultado = cadena.replace(cadena_parentesis, cadena_invertida)

    if '(' in cadena_resultado:
        return n_reversion(cadena_resultado)
    else:
        return cadena_resultado


print(n_reversion(cadena4))


# def n_reversion(cadena):
#     while '(' in cadena:
#         # Encontrar el último paréntesis de apertura
#         ini = cadena.rfind('(')
#         # Encontrar el primer paréntesis de cierre después del último paréntesis de apertura
#         fin = cadena.find(')', ini)
        
#         # Obtener la subcadena que necesita ser invertida
#         cadena_parentesis = cadena[ini+1:fin]
        
#         # Invertir la subcadena
#         cadena_invertida = cadena_parentesis[::-1]
        
#         # Reemplazar la subcadena original (con paréntesis) por la subcadena invertida (sin paréntesis)
#         cadena = cadena[:ini] + cadena_invertida + cadena[fin+1:]
    
#     return cadena

# print(n_reversion(cadena4)) 