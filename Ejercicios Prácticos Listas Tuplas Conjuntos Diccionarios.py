
lista = [1,2,3,4,5]
lista.append(6)
print(lista)

lista[1] *= 2
print(lista)

lista.insert(2, 'dos y medio')
print(lista)

shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
print(shopping)
#shopping = '|'.join(shopping) #La función 'join' une los elementos de una lista con un separador y los convierte en una cadena de texto
#print(type(shopping))

for i, product in enumerate(shopping): #'enumerate' es una función que nos muestra el indice de los elementos de la lista
    print(i, product)

tupla = ('Bogotá', 'Pasto', 'Cartagena')
#tupla[1] = 'Medellin' Las tuplas son inmutables; no se pueden cambiar

print(tupla[1])


conjunto_uno = {1,5,1,6,2}
conjunto_dos = {3,4,4,6,7}

print(conjunto_dos)

conjunto_uno.add(9)

print(conjunto_uno)

#Unión de conjuntos

union_conjuntos = conjunto_uno | conjunto_dos
print(union_conjuntos)

intersección_conjuntos = conjunto_uno & conjunto_dos
print(intersección_conjuntos)


#Diccionarios
diccionario = {
    'Diana' : 19,
    'Jose' : 27
}

print(diccionario)

diccionario['Sachita'] = 'Es una cachora muy bonita'
print(diccionario)

print(diccionario.keys()) #Acceder UNICAMENTE a las llaves
print(diccionario.values()) #Acceder UNICAMENTE a los valores

for llaves in diccionario.keys():
    print(llaves)

for valores in diccionario.values():
    print(valores)

for elementos in diccionario.items():
    print(elementos)




cadena = "Hola Mundo"

print(cadena[::-1])

cadena2 = "Hola Mundo"
nueva_cadena = ""

for letra in cadena2:
    nueva_cadena = letra + nueva_cadena

print(nueva_cadena)