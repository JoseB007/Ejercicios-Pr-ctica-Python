# Santa 🎅 está probando su nuevo trineo eléctrico, el CyberReindeer, en una carretera del Polo Norte. La carretera se representa con una cadena de caracteres, donde:

# . = Carretera
# S = Trineo de Santa
# * = Barrera abierta
# | = Barrera cerrada
# Ejemplo de carretera: S..|...|..

# Cada unidad de tiempo, el trineo avanza una posición a la derecha. Si encuentra una barrera cerrada, se detiene hasta que la barrera se abra. Si está abierta, la atraviesa directamente.

# Todas las barreras empiezan cerradas, pero después de 5 unidades de tiempo, se abren todas para siempre.

# Crea una función que simule el movimiento del trineo durante un tiempo dado y devuelva un array de cadenas representando el estado de la carretera en cada unidad de tiempo

def cyberReindeer(road, time):
  
    return

road = 'S..|...|..'
time = 10

print(cyberReindeer(road, time))


# def listaOrdenada(lista):
#     n = len(lista)
#     for i in range(0, n):
#         for j in range(0, n-i-1):
#             print(j, end='')
#             if lista[j] > lista[j + 1]:
#                 lista[j], lista[j + 1] = lista[j + 1], lista[j]

#     return lista
            
# lista = [7,6,8,1,4]
# print(listaOrdenada(lista))
