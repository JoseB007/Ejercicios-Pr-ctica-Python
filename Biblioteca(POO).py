
# Creación de la clase Libro
class Libro:
    def __init__(self):
        self.titulo = ""
        self.autor = ""
        self.año_publicacion = 0
        self.calificacion = 0
        pass

    def ingresar_informacion(self):
        self.titulo = input('Ingrese el título del libro: ')
        self.autor = input('Ingrese el autor del libro: ')

        while True:
            try:
                self.año_publicacion = int(input('Ingrese el año de la publicación del libro: '))
                break
            except ValueError:
                print('Por favor ingrese un año válido')
        
        while True:
            try:
                self.calificacion = int(input('Ingrese la calificación del libro (1-5): '))
                if self.calificacion >= 1 and self.calificacion <= 5:
                    break
                else:
                    print('La calificación debe estar entre el rango de 1 a 5')
            except ValueError:
                print('Por favor ingrese una calificación valida')
    
lista_libros = []

while True:
    # Creación de las Instancias u Objetos
    nuevo_libro = Libro()
    # Llamada a los métodos
    nuevo_libro.ingresar_informacion()

    lista_libros.append(nuevo_libro)

    ingresar_nuevo_libro = input('¿Desea agregar un nuevo libro? (Sí/No): ').lower()

    if ingresar_nuevo_libro != 'si':
        break

for index, libro in enumerate(lista_libros, start=1):
    print(f'\n Libro {index}:\nTítulo: {libro.titulo}\nAutor: {libro.autor}\nAño: {libro.año_publicacion}\nCalificación: {libro.calificacion}\n')