
class Tarea:
    def __init__(self, nombre, descripcion, fecha_inicio, fecha_final) -> None:
        self.nombre = nombre
        self.descripcion = descripcion
        self.F_inicio = fecha_inicio
        self.F_final = fecha_final
        self.completada = False
        pass
    
    def completar_tarea(self):
        self.completada = True
    
    def obtener_informacion(self):
        estado = "Completada" if self.completada else "Pendiente"
        return self.nombre, self.descripcion, self.F_inicio, self.F_final, estado

class Proyecto:
    def __init__(self, nombre, descripcion, fecha_inicio, fecha_final) -> None:
        self.nombre = nombre
        self.descripcion = descripcion
        self.F_inicio = fecha_inicio
        self.F_final = fecha_final
        self.tareas = []
        pass

    def asignar_tareas(self, tarea):
        self.tareas.append(tarea)
        
class Usuario:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.proyectos = []
        pass

    def crear_proyecto(self, proyecto):
        self.proyectos.append(proyecto)

    def asignar_tarea_al_proyecto(self, tarea, proyecto):
        proyecto.asignar_tareas(tarea)

    def marcar_tarea_completada(self, tarea):
        tarea.completar_tarea()

    def mostrar_proyectos(self):
        print(f'\nUsuario: {self.nombre}')
        for indice, proyecto in enumerate(self.proyectos, start= 1):
            print(f'\nProyecto No. {indice}\n{proyecto.nombre}\nDescripción\n{proyecto.descripcion}\nFecha de Inicio: {proyecto.F_inicio}\nFecha de Finalización: {proyecto.F_final}')
            for tarea in proyecto.tareas:
                print(f"\nTareas de proyecto:\n  - {tarea.obtener_informacion()}")


            
usuario1 = Usuario(nombre="Jose")
usuario2 = Usuario(nombre="Diana")

proyecto1 = Proyecto(nombre="Mi primera Página Web", descripcion="Creación de una página web utilizando HTML y CSS", fecha_inicio="23/02/2024", fecha_final="01/03/2024")
proyecto2 = Proyecto(nombre="Mi primer registro", descripcion="Creación de un registro contable", fecha_inicio="23/02/2024", fecha_final="01/03/2024")
proyecto3 = Proyecto(nombre="Mi primera Base de Datos", descripcion="Creación de una base de datos en MySql", fecha_inicio="23/02/2024", fecha_final="01/03/2024")

tarea1 = Tarea(nombre="Diseñar Maquetación en HTML", descripcion="Hacer el diseño de la página web a través del lenguaje de maquetación HTML", fecha_inicio="23/02/2024", fecha_final="24/02/2024")

tarea2 = Tarea(nombre="Diseñar la estructura de una base de datos", descripcion="Crear tabla de usuarios, documento y ocupación en una base de datos en MySql", fecha_inicio="23/02/2024", fecha_final="24/02/2024")

usuario1.crear_proyecto(proyecto1)
usuario1.crear_proyecto(proyecto2)
usuario1.crear_proyecto(proyecto3)
usuario1.asignar_tarea_al_proyecto(tarea1, proyecto1)
usuario1.asignar_tarea_al_proyecto(tarea2, proyecto3)
usuario1.marcar_tarea_completada(tarea1)
usuario1.mostrar_proyectos()

usuario2.crear_proyecto(proyecto2)
usuario2.mostrar_proyectos()
