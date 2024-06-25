# En el taller de Santa, un elfo travieso ha estado jugando en la cadena de fabricación de regalos, añadiendo o eliminando un paso no planificado.

# Tienes la secuencia original de pasos en la fabricación original y la secuencia modificada modified que puede incluir un paso extra o faltar un paso.

# Tu tarea es escribir una función que identifique y devuelva el primer paso extra que se ha añadido o eliminado en la cadena de fabricación. Si no hay ninguna diferencia entre las secuencias, devuelve una cadena vacía.


original = 'ste4'
modified = 'stex56'

def findNaughtyStep(original, modified):
    if len(modified) > len(original):
        for p in modified:
            if p not in original:
                return p
    elif len(modified) == len(original):
        for p in modified:
            if p not in original:
                return p
    else:
        for p in original:
            if p not in modified:
                return p
    return ""

        
print(findNaughtyStep(original, modified))