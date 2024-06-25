
def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return 'ERROR, División por cero'
    
def calculadora_basica():

    while True:
    #Se inicia un bucle infinito hasta que el usuario decida salir del bucle
        print('Opción 1: Sumar')
        print('Opción 2: Restar')
        print('Opción 3: Multiplicar')
        print('Opción 4: Dividir')
        print('Opción 5: Salir')

        try:
            opcion = int(input('Escoja una opción: '))

            if opcion == 5:
                #Si el usuario digita el número 5 el programa sale del bucle infinito
                break
            elif opcion in (1, 2, 3, 4):
                num1 = int(input('Digite el primer número: '))
                num2 = int(input('Digite el segundo número: '))

                if opcion == 1:
                    print(f'El resultado es: {sumar(num1, num2)}')
                elif opcion == 2:
                    print(f'El resultado es: {restar(num1, num2)}')
                elif opcion == 3:
                    print(f'El resultado es: {multiplicar(num1, num2)}')
                elif opcion == 4:
                    print(f'El resultado es: {dividir(num1, num2)}')
            else: print('Opción no valida')
        except ValueError:
            print('Opción no valida')

if __name__ == "__main__":
    calculadora_basica()