
def buscar_primer_numero_repetido(lista):
    conjunto_auxiliar = set()

    for num in lista:
        if num not in conjunto_auxiliar:
            conjunto_auxiliar.add(num)
        else:
            return num

lista = [2, 1, 4, 4, 3, 1, 5, 3, 2]
resultado = buscar_primer_numero_repetido(lista)
print(f'El primer número que se repite en la lista es el {resultado}')


def regalos_que_se_pueden_fabricar(lista_regalos, materiales_disponibles):
    regalos_fabricables = []

    for regalo in lista_regalos:
        if all(letra in materiales_disponibles for letra in regalo):
            regalos_fabricables.append(regalo)
            
    return regalos_fabricables

# Ejemplo de uso:
lista_regalos = ['tren', 'oso', 'pelota', 'caramelo']
materiales_disponibles = 'tronesa'

regalos_fabricables = regalos_que_se_pueden_fabricar(lista_regalos, materiales_disponibles)
print("Regalos que se pueden fabricar:", regalos_fabricables)


def encontrar_elemento_modificado(lista_original, lista_modificada):
    lista_elementos_modificados = []

    for objeto in lista_modificada:
        if objeto not in lista_original:
            lista_elementos_modificados.append(objeto)

    return lista_elementos_modificados

original = 'abcd'
modified = 'ab cdei '

elemento_modificado = encontrar_elemento_modificado(original, modified)
print(f'El elemento que se modificó es: {elemento_modificado}')


