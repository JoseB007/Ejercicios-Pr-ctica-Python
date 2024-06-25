# Están encendiendo las luces de Navidad 🎄 en la ciudad y, como cada año, ¡hay que arreglarlas!

# Las luces son de dos colores: 🔴 y 🟢 . Para que el efecto sea el adecuado, siempre deben estar alternadas. Es decir, si la primera luz es roja, la segunda debe ser verde, la tercera roja, la cuarta verde, etc.

# Nos han pedido que escribamos una función adjustLights que, dado un array de strings con el color de cada luz (representados con los emojis 🔴 para el rojo y 🟢 para el verde), devuelva el número mínimo de luces que hay que cambiar para que estén los colores alternos.

def adjustLights(luces):
    patron1 = []
    patron2 = []
    v = '🟢'
    r = '🔴'
    for i in range(len(luces)):
        if i % 2 == 0:
            patron1.append(r)
        elif i % 2 != 0:
            patron1.append(v)

    for i in range(len(luces)):
        if i % 2 == 0:
            patron2.append(v)
        elif i % 2 != 0:
            patron2.append(r)

    contador1 = 0
    contador2 = 0
    indicesPatro1 = []
    indicesPatro2 = []

    for i in range(len(luces)):
        if luces[i] != patron1[i]:
            contador1 += 1
            indicesPatro1.append(i)

    for i in range(len(luces)):
        if luces[i] != patron2[i]:
            contador2 += 1
            indicesPatro2.append(i)

    print(f'Se requiere hacer {min(contador1, contador2)} cambio(s)')

    if len(indicesPatro1) < len(indicesPatro2):
        for i in indicesPatro1:
            print(f'Cambia la luz {(i)+1} a {patron1[i]}')
    else:
        for i in indicesPatro2:
            print(f'Cambia la luz {(i)+1} a {patron2[i]}')

           
luces = ['🟢', '🔴', '🔴', '🔴', '🟢']
adjustLights(luces)