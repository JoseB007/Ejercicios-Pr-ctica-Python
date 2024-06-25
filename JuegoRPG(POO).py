import random

class Jugador:
    def __init__(self, nombre, hp=100, atk=0 , deff=0):
        self.nombre = nombre
        self.hp = hp
        self.atk = atk
        self.deff = deff

    def atacar(self, objetivo):
       if objetivo.hp > 0:
            danio = random.randint(1, objetivo.hp)
            objetivo.hp -= danio
            print(f'{self.nombre} ataca a {objetivo.nombre} y le inflige {danio} puntos de daño')

    def informacion(self):
        print(f' - Nombre: {self.nombre}\n - HP: {self.hp}')

class Monstruo:
    def __init__(self, nombre, hp=100, atk=0, deff=0):
        self.nombre = nombre
        self.hp = hp
        self.atk = atk
        self.deff = deff

    def atacar(self, objetivo):
        if objetivo.hp > 0:
            danio = random.randint(1, objetivo.hp)
            objetivo.hp -= danio
            print(f'{self.nombre} ataca a {objetivo.nombre} y le inflige {danio} puntos de daño')
    
    def informacion(self):
        print(f' - Nombre: {self.nombre}\n - HP: {self.hp}')


class Juego:
    def __init__(self, jugador, monstruo):
        self.jugador = jugador
        self.monstruo = monstruo

    def simular_juego(self):
        while self.jugador.hp > 0 and self.monstruo.hp > 0:

            self.jugador.atacar(self.monstruo)
            if self.monstruo.hp <= 0:
                print(f'\n - El {self.jugador.nombre} ha derrotado al {self.monstruo.nombre}')
                break

            self.monstruo.atacar(self.jugador)
            if self.jugador.hp <= 0:
                print(f'\n - El {self.monstruo.nombre} ha derrotado al {self.jugador.nombre}')
                break

        print("\nInformación del Jugador")
        jugador.informacion()
        print("Información del Monstruo")
        monstruo.informacion()
        
jugador = Jugador(nombre="Heroe")
monstruo = Monstruo(nombre="Orco")
juego1 = Juego(jugador, monstruo)

juego1.simular_juego()
