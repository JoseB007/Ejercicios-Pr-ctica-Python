#  * Crea una función que evalúe si un/a atleta ha superado correctamente una
#  * carrera de obstáculos.
#  * - La función recibirá dos parámetros:
#  *      - Un array que sólo puede contener String con las palabras
#  *        "run" o "jump"
#  *      - Un String que represente la pista y sólo puede contener "_" (suelo)
#  *        o "|" (valla)
#  * - La función imprimirá cómo ha finalizado la carrera:
#  *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
#  *        será correcto y no variará el símbolo de esa parte de la pista.
#  *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
#  *      - Si hace "run" en "|" (valla), se variará la pista por "/".
#  * - La función retornará un Boolean que indique si ha superado la carrera.
#  * Para ello tiene que realizar la opción correcta en cada tramo de la pista.


def evaluaCarrera(pista, atleta):
    nueva_pista = ""
    for i in range(len(pista)):
        if (pista[i] == '.' and atleta[i] == 'run') or (pista[i] == '|' and atleta[i] == 'jump'):
            nueva_pista += pista[i]
        elif pista[i] == '.' and atleta[i] != 'run':
            nueva_pista += 'x'
        elif pista[i] == '|' and atleta[i] != 'jump':
            nueva_pista += '/'
    
    if nueva_pista == pista:
        return 'Carrera terminada satisfactoriamente!'
    else:
        return nueva_pista


pista = "..|..|.."
atleta = ['run', 'run', 'jump', 'run', 'run', 'jump', 'run', 'run']
print(evaluaCarrera(pista, atleta))

pista2 = "..|..|.."
atleta2 = ['run', 'jump', 'jump', 'run', 'run', 'jump', 'run', 'run']
print(evaluaCarrera(pista2, atleta2))