# Clase Padre
class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
        pass

    def saludar(self):
        print(f'Hola, soy {self.nombre} y tengo {self.edad} años')

# Clase Hijo - Herencia
class Estudiante(Persona):
    def __init__(self, nombre, edad, curso) -> None:
        super().__init__(nombre, edad)
        self.curso = curso

    def estudiar(self):
        print(f'{self.nombre} está estudiando en el curso {self.curso}')

persona1 = Estudiante('Diana', 19, 'Universitario')
persona1.saludar()
persona1.estudiar()

# Creación de la Clase

class Perro:
    def __init__(self, nombre, raza) -> None:
        self.nombre = nombre
        self.raza = raza
        pass

    def ladrar(self):
        print(f'{self.nombre} está ladrando')

# Creación de las Instancias u Objetos

perro1 = Perro('Scoot', 'Labrador')
perro2 = Perro('Morena', 'Salchicha')

# Acceder a los atributos y llamar métodos

print(f'{perro1.nombre} es un perro de la raza {perro1.raza}')
perro2.ladrar()

# Creación de la clase Circulo
class Circulo:
    def __init__(self, radio) -> None:
        self.radio = radio
        pass

    def calcular_area(self):
        return self.radio * 3.14
    
# Creación de las Instancias
circulo1 = Circulo(10)
# Acceder a los atributos y llamar métodos
print(f'El área del círculo es {circulo1.calcular_area()}')

class Pelicula:
    def __init__(self, titulo, director, duracion) -> None:
        self.titulo = titulo
        self.director = director
        self.duracion = duracion
        pass

    def mostrar_informacion(self):
        duracion_horas = self.duracion * 1 / 60
        print(f'\nNombre de la película: {self.titulo}\nDirector: {self.director}\nDuración de la película en horas: {duracion_horas}')
    
pelicula1 = Pelicula(titulo="Titanic", director="James Cameron", duracion=80)
pelicula2 = Pelicula(titulo="Hombres de Negro", director="Barry Sonnenfeld", duracion=72)
pelicula3 = Pelicula(titulo="Guardianes de la Galaxia", director="James Gunn", duracion=145)
pelicula1.mostrar_informacion()
pelicula2.mostrar_informacion()
pelicula3.mostrar_informacion()