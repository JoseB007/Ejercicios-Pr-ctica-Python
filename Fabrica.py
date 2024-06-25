# En el taller de Santa, los elfos tienen una lista de regalos que desean fabricar y un conjunto limitado de materiales.

# Los regalos son cadenas de texto y los materiales son caracteres. Tu tarea es escribir una función que, dada una lista de regalos y los materiales disponibles, devuelva una lista de los regalos que se pueden fabricar.

# Un regalo se puede fabricar si contamos con todos los materiales necesarios para fabricarlo.

regalos = ["carro", "muñeca", "pelota", "robot"]
materials = 'carouñecapelotarob'

def consultar(regalos, materials):
    regalos_fabricados = []
    for regalo in regalos:
        for char in regalo:
            if char not in materials:
                break
        else:
            regalos_fabricados.append(regalo)
    
    return regalos_fabricados
            

print(consultar(regalos, materials))
