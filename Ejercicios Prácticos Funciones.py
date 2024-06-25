
def saludar(nombre):
    #Función que toma como parámetro un nombre y devuelve un saludo personalizado
    return f'¡Hola, {nombre}!'

nombre = 'Daniel'

resultado_saludar = saludar(nombre)
print(resultado_saludar)

def suma_pares(numero):
    #Función que toma como parámetro un número y devuelve la suma de todos los números pares hasta el número dado
    suma = 0
    for i in range(2, numero + 1, 2):
        suma += i

    return suma

numero = 6

resultado_suma_pares = suma_pares(numero)
print(f'La suma de todos los números pares hasta el número ingresado es: {resultado_suma_pares}')

def es_palindromo(palabra):
    #Función que toma como argumento una cadena de texto y comprueba si se leé exactamenete al derecho como al revés
    if palabra == palabra[::-1]:
        return True
    else: return False

print(es_palindromo('hannah'))
print(es_palindromo('amar'))
print(es_palindromo('radar'))

def es_primo(numero_primo):
    #Función que toma como argumento un número y comprueba si es un número primo
    for i in range(2, numero_primo):
        if numero_primo % i == 0:
            return False
    return True

numero = 15
resultado_es_primo = es_primo(numero)
print(resultado_es_primo)

def fibonacci(n):
    # Inicializar la lista para almacenar la serie Fibonacci
    serie = [0, 1]

    # Generar la serie Fibonacci hasta alcanzar la longitud deseada
    for i in range(n):
        siguiente_numero = serie[-1] + serie[-2]
        serie.append(siguiente_numero)
    
    return serie

# Ejemplos de uso
print(fibonacci(5))
print(fibonacci(10))

def convertir_temperatura(temp):
    formula = (temp*9/5) + 32

    return formula

print(convertir_temperatura(18))

def contar_palabras(text):
    contador = len(text.split())

    return contador

print(contar_palabras('Habia una vez un barco chiquito'))
print(contar_palabras('Mi amor Bonita'))  

def contar_vocales(texto):
    vocales = ['a','e','i','o','u']

    for vocal in vocales:
        contador = texto.count(vocal) 
        print(f'La vocal {vocal} se encontró {contador} veces')
    

contar_vocales('habia una vez')


def es_primo_lista(lista):
    for numero in lista:
        es_primo = True
        for i in range(2, numero):
            if numero % i == 0:
                es_primo = False
                break
        if es_primo:
            print(f'{numero} es primo')
        else:
            print(f'{numero} no es primo')

lista_primos = [15, 2, 5, 9, 17, 6]
es_primo_lista(lista_primos)
