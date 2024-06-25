#  * Crea un programa que comprueba si los paréntesis, llaves y corchetes
#  * de una expresión están equilibrados.
#  * - Equilibrado significa que estos delimitadores se abren y cieran
#  *   en orden y de forma correcta.
#  * - Paréntesis, llaves y corchetes son igual de prioritarios.
#  *   No hay uno más importante que otro.
#  * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
#  * - Expresión no balanceada: { a * ( c + d ) ] - 5 }


def comprobarExpresion(cadena):
    expresiones_abiertas = ['{', '(', '[']
    expresiones_cerradas = ['}', ')', ']']

    cadena_expresiones = ""
    cadena_expresiones_abiertas = ""
    cadena_expresiones_cerradas = ""

    for i in cadena:
        if i in expresiones_abiertas:
            cadena_expresiones += i
            cadena_expresiones_abiertas += i
        elif i in expresiones_cerradas:
            cadena_expresiones += i

    if cadena_expresiones[0] in expresiones_cerradas:
        return f'Error! No se puede inciar con "{cadena_expresiones[0]}" sin antes haber una expresión de apertura'
    
    for j in cadena_expresiones_abiertas:
        indice_expresion_abierta = expresiones_abiertas.index(j)
        expresion_cerrada = expresiones_cerradas[indice_expresion_abierta]
        cadena_expresiones_cerradas += expresion_cerrada
        
    invertir_expresiones_cerradas = cadena_expresiones_cerradas[::-1]
    cadena_expresiones_balanceada = cadena_expresiones_abiertas + invertir_expresiones_cerradas

    lista_expresiones_balanceadas = list(cadena_expresiones_balanceada)

    cadena_expresiones += ('*' * (len(cadena_expresiones_balanceada) - len(cadena_expresiones)))
    
    inicio = 0
    fin = len(cadena_expresiones_balanceada)-1
    while inicio < fin:                
        if cadena_expresiones[inicio] in expresiones_abiertas:
            indice_expresion = expresiones_abiertas.index(cadena_expresiones[inicio])
            expresion_esperada = expresiones_cerradas[indice_expresion]
            lista_expresiones_balanceadas[inicio] = cadena_expresiones[inicio]
            lista_expresiones_balanceadas[fin] = expresion_esperada

            inicio += 1
            fin -= 1 

        elif cadena_expresiones[inicio] in expresiones_cerradas:
            indice_expresion = expresiones_cerradas.index(cadena_expresiones[inicio])
            expresion_esperada = expresiones_abiertas[indice_expresion]
            
            if cadena_expresiones[inicio-1] == expresion_esperada:
                lista_expresiones_balanceadas[inicio] = cadena_expresiones[inicio]

            inicio += 1
            fin += 1 

    cadena_expresiones_finales = ''.join(map(str, lista_expresiones_balanceadas))

    if len(cadena_expresiones) > len(cadena_expresiones_finales):
        return f'Error! Hacen faltan expresiones de apertura'
    
    for expresion in range(len(cadena_expresiones_finales)):
        if cadena_expresiones[expresion] != cadena_expresiones_finales[expresion]:
            return f'Error! se espera "{cadena_expresiones_finales[expresion]}" como expresión de cierre en la posición número {expresion+1} de las expresiones'
    else:
        return 'Todas las expresiones están completamente balanceadas'
    
    
cadena = '{ a * } {[() c + d - 5 ]}'
print(comprobarExpresion(cadena))