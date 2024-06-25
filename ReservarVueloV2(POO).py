
class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, fecha_salida, hora_salida, asientos_totales, asientos_disponibles) -> None:
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha_salida = fecha_salida
        self.hora_salida = hora_salida
        self.asientos_totales = asientos_totales
        self.asientos_disponibles = asientos_disponibles
        self.pasajeros_asignados = []
        pass

    def consultar_vuelo(self):
        print(f'\nNo. Vuelo: {self.numero_vuelo}')
        print(f'Origen: {self.origen}')
        print(f'Destino: {self.destino}')
        print(f'Fecha de Salida: {self.fecha_salida}')
        print(f'Hora de Salida: {self.hora_salida}')
        print(f'Asientos Totales: {self.asientos_totales}')
        print(f'Asientos Disponibles: {self.asientos_disponibles}')

    def reservar_vuelo(self, nombre, apellido, identificacion, num_asiento):
        if self.asientos_disponibles > 0:
            if num_asiento not in self.pasajeros_asignados:
                nuevo_pasajero = Pasajero(nombre, apellido, identificacion)
                self.pasajeros_asignados.append((nuevo_pasajero, num_asiento))
                self.asientos_disponibles -= 1
                return print(f'\nAsiento No. {num_asiento} reservado con éxito en el vuelo No. {self.numero_vuelo}')
            else:
                return print('\nEl asiento no está disponible')
        else:
            print('\nLo siento, no hay asientos disponibles')

    def consultar_pasajeros(self):
        for index, (pasajero, num_asiento) in enumerate(self.pasajeros_asignados, start=1):
            print(f'\nPasajero: {index}\nPasajero: {pasajero.nombre} {pasajero.apellido}\nIdentificación: {pasajero.identificacion}\nNo. Vuelo: {self.numero_vuelo}\nOrigen: {self.origen}\nDestino: {self.destino}\nNo. Asiento: {num_asiento}')


class Pasajero:
    def __init__(self, nombre, apellido, identificacion) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.identificacion = identificacion
        pass


vuelo1 = Vuelo(numero_vuelo= '1', origen= 'Colombia', destino= 'Japón', fecha_salida= '17/02/204', hora_salida= '5:00 p.m.', asientos_totales= 130, asientos_disponibles= 130)
vuelo2 = Vuelo(numero_vuelo= '2', origen= 'EE.UU', destino= 'Colombia', fecha_salida= '17/02/204', hora_salida= '3:00 p.m.', asientos_totales= 110, asientos_disponibles= 105)

while True:
    print('\nEscoja una opción: \n')
    print('Opción 1: Consultar Vuelos')
    print('Opción 2: Reservar un vuelo')
    print('Opción 3: Consultar pasajeros')
    print('Opción 4: Salir')

    try:
        escojer_opcion = int(input('Ingrese una opción: '))
        if escojer_opcion == 4:
            break
        elif escojer_opcion == 1:
            consultar_vuelo = vuelo1.consultar_vuelo(), vuelo2.consultar_vuelo()
        elif escojer_opcion == 2:
            nombre_pasajero = input('\nIngrese su nombre: ')
            apellido_pasajero = input('Ingrese su apellido: ')
            identificacion = input('Ingrese su No. de indentificación: ')
            num_asiento = input('Ingrese el No. de asiento que desea reservar: ')
            reservar_no_vuelo = input('Ingrese el No. de vuelo que desea reservar (o "salir" para finalizar): ')

            if reservar_no_vuelo == "1":
                vuelo1.reservar_vuelo(nombre_pasajero, apellido_pasajero, identificacion, num_asiento)
            elif reservar_no_vuelo == "2":
                vuelo2.reservar_vuelo(nombre_pasajero, apellido_pasajero, identificacion, num_asiento)
            else: print('Vuelo no encontrado')
        elif escojer_opcion == 3:
            consultar_pasajeros = vuelo1.consultar_pasajeros(), vuelo2.consultar_pasajeros()
    except ValueError:
        print('La opción no es válida')