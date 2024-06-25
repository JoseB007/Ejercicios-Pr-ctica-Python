class Empleado:
    def __init__(self, nombre, documento) -> None:
        self.nombre = nombre
        self.documento = documento

    def informacion(self):
        info = f'  - Nombre del empleado: {self.nombre}\n  - Documento: {self.documento}'
        return info
      
class Departamento():
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.lista_empleados = []

    def asignar_empleado(self, empleado):
        self.lista_empleados.append(empleado)

    def obtener_empleados(self):
        return self.lista_empleados

class Empresa():
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.lista_de_empleados = []
        self.lista_de_departamentos = []

    def asignar_empleado(self, empleado):
        self.lista_de_empleados.append(empleado)

    def asignar_departamento(self, departamento):
        self.lista_de_departamentos.append(departamento)

    def asignar_empleado_a_departamento(self, departamento, empleado):
        departamento.asignar_empleado(empleado)
        
    def obtener_informacion(self):
        info_empresa = f'\nEmpresa: {self.nombre}'
        info_departamentos = []

        for departamento in self.lista_de_departamentos:
            info_departamento = f'\nNombre del departamento: {departamento.nombre}\n'
            empleados_departamento = [e.informacion() for e in departamento.obtener_empleados()]
            info_departamento += '\n'.join(empleados_departamento)
            info_departamentos.append(info_departamento)

        return info_empresa + '\n'.join(info_departamentos)
        

empresa = Empresa(nombre="Postobón")
departamento1 = Departamento(nombre="Ventas")
departamento2 = Departamento(nombre="Contabilidad")

empleado1 = Empleado(nombre="Jose", documento="1085331402")
empleado2 = Empleado(nombre="Diana", documento="1081274283")
empleado3 = Empleado(nombre="Marlon", documento="1085431726")

empresa.asignar_departamento(departamento1)
empresa.asignar_departamento(departamento2)

empresa.asignar_empleado(empleado1)
empresa.asignar_empleado_a_departamento(departamento1, empleado1)

empresa.asignar_empleado(empleado2)
empresa.asignar_empleado_a_departamento(departamento1, empleado2)

empresa.asignar_empleado(empleado3)
empresa.asignar_empleado_a_departamento(departamento2, empleado3)

print(empresa.obtener_informacion())
##########################################################################################################
empresa_asus = Empresa(nombre="ASUS")
departamento_asus1 = Departamento(nombre="Gerencia")
empleado_asus1 = Empleado(nombre="Daniel", documento="98385103")

empresa_asus.asignar_departamento(departamento_asus1)
empresa_asus.asignar_empleado(empleado_asus1)
empresa_asus.asignar_empleado_a_departamento(departamento_asus1, empleado_asus1)
print(empresa_asus.obtener_informacion())
