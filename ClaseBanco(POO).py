class Cliente:
    def __init__(self, nombre, saldo_inicial=0):
        self.nombre = nombre
        self.saldo = saldo_inicial

    def obtener_nombre(self):
        return self.nombre

    def obtener_saldo(self):
        return self.saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"{self.nombre} ha hecho un depósito de {cantidad}. Nuevo saldo: {self.saldo}")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"{self.nombre} retiró {cantidad} de su saldo. Nuevo saldo: {self.saldo}")
        else:
            print("Saldo insuficiente. Retiro no procesado.")


class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"{cliente.obtener_nombre()} se ha convertido en cliente de {self.nombre}.")

    def mostrar_clientes(self):
        print(f"Clientes de {self.nombre}:")
        for cliente in self.clientes:
            print(f"- {cliente.obtener_nombre()}")

    def calcular_saldo_total(self):
        saldo_total = sum(cliente.obtener_saldo() for cliente in self.clientes)
        print(f"Saldo total de todos los clientes: {saldo_total}")


# Ejemplo de uso
cliente1 = Cliente("Alice", 1000)
cliente2 = Cliente("Bob", 500)

banco = Banco("Mi Banco")
banco.agregar_cliente(cliente1)
banco.agregar_cliente(cliente2)

cliente1.depositar(200)
cliente2.retirar(50)

banco.mostrar_clientes()
banco.calcular_saldo_total()
