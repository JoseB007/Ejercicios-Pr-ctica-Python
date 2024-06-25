
class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, fecha_salida, hora_salida, asientos_totales, asientos_disponibles) -> None:
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha_salida = fecha_salida
        self.hora_salida = hora_salida
        self.asientos_totales = asientos_totales
        self.asientos_disponibles = asientos_disponibles
        self.asientos_reservados = []
        pass

    def reservar_asiento(self, pasajero, num_asiento):
        if num_asiento <= self.asientos_disponibles:
            if num_asiento not in self.asientos_reservados:
                self.asientos_reservados.append({
                    'num_asiento': num_asiento,
                    'nombre_pasajero': pasajero.nombre,
                    'apellido_pasajero': pasajero.apellido,
                    'identificacion_pasajero': pasajero.identificacion,
                    'numero_pasaporte_pasajero': pasajero.numero_pasaporte
                })      
                print(f'Asiento {num_asiento} reservado con éxito\n')
                self.asientos_disponibles -= 1
            else:
                print(f'El asiento {num_asiento} ya está reservado')
        else:
            print('El número de asiento ingresado no es válido')

    def obtener_informacion_vuelo(self):
        print(f'\nNo. Vuelo: {self.numero_vuelo}')
        print(f'Origen: {self.origen}')
        print(f'Destino: {self.destino}')
        print(f'Fecha de salida: {self.fecha_salida}')
        print(f'Hora de salida: {self.hora_salida}')
        print(f'Asientos Totales: {self.asientos_totales}')
        print(f'Asientos Disponibles: {self.asientos_disponibles}')
        print(f'Asientos Reservados: {self.asientos_reservados}')
        pass

    def obtener_informacion_pasajero_vuelo(self):
        for pasajero in self.asientos_reservados:
            print(f'No. Vuelo: {self.numero_vuelo}\nOrigen: {self.origen}\nDestino: {self.destino}\nFecha de salida: {self.fecha_salida}\nHora de salida: {self.hora_salida}\nPasajero: {pasajero["nombre_pasajero"]} {pasajero["apellido_pasajero"]}\nIdentificación: {pasajero["identificacion_pasajero"]}\nNo. Pasaporte: {pasajero["numero_pasaporte_pasajero"]}\nNo. Asiento: {pasajero["num_asiento"]}\n')

class Pasajero:
    def __init__(self, nombre, apellido, identificacion, numero_pasaporte) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.identificacion = identificacion
        self.numero_pasaporte = numero_pasaporte
        pass 

    def reservar_asiento(self, vuelo):
        num_asiento = int(input(f'Ingrese el número de asiento que desea reservar en el vuelo número {vuelo.numero_vuelo}: '))

        # Se está llamando al método reservar_asiento de la clase Vuelo y se le está pasando como argumento la variable num_asiento.
        vuelo.reservar_asiento(self, num_asiento)


vuelo1 = Vuelo(numero_vuelo= 1, origen= 'Colombia', destino= 'Japón', fecha_salida= '17/02/204', hora_salida= '5:00 p.m.', asientos_totales= 130, asientos_disponibles= 130)
vuelo2 = Vuelo(numero_vuelo= 2, origen= 'EE.UU', destino= 'Colombia', fecha_salida= '17/02/204', hora_salida= '3:00 p.m.', asientos_totales= 130, asientos_disponibles= 130)
pasajero1 = Pasajero(nombre= 'Jose', apellido= 'Botina', identificacion= '1085331402', numero_pasaporte= 1996)
pasajero2 = Pasajero(nombre= 'Diana', apellido= 'Rosero', identificacion= '1085331502', numero_pasaporte= 2005) 
pasajero3 = Pasajero(nombre= 'Daniel', apellido= 'Botina', identificacion= '1085331802', numero_pasaporte= 2001)                  

pasajero1.reservar_asiento(vuelo1)
pasajero2.reservar_asiento(vuelo1)
pasajero3.reservar_asiento(vuelo2)

vuelo1.obtener_informacion_pasajero_vuelo()
vuelo2.obtener_informacion_pasajero_vuelo()

