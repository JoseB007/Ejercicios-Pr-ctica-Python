
class Producto:
    def __init__(self, nombre, precio, descripcion) -> None:
        self.nombre_producto = nombre
        self.precio_producto = precio
        self.descripcion_producto = descripcion
        pass

    def obtener_nombre(self):
        return self.nombre_producto
    
    def obtener_precio(self):
        return self.precio_producto

class Carrito:
    def __init__(self) -> None:
        self.productos_carrito = []
        pass

    def agregar_producto(self, producto):
        self.productos_carrito.append(producto)
        print(f'{producto.obtener_nombre()} añadido con éxito al carrito')

    def calcular_total(self):
        valor_total = sum(producto.obtener_precio() for producto in self.productos_carrito)
        print(f'\nEl valor total del carrito es de: {valor_total}')

class Cliente:
    def __init__(self, nombre) -> None:
        self.nombre_cliente = nombre
        self.carrito = Carrito()
        pass

    def agregar_producto_al_carrito(self, producto):
        self.carrito.agregar_producto(producto)

    def calcular_valor_productos(self):
        self.carrito.calcular_total()

    def mostrar_mi_carrito(self):
        print(f'\nCliente: {self.nombre_cliente}\nMi carrito:\n')
        for producto in self.carrito.productos_carrito:
            print(f'Producto: {producto.nombre_producto}\nPrecio: {producto.precio_producto}')



cliente1 = Cliente(nombre="Jose")
cliente2 = Cliente(nombre="Diana")
producto1 = Producto(nombre="Detergente", precio=1500, descripcion="Ariel")
producto2 = Producto(nombre="Arroz", precio=1100, descripcion="Manuelita")
producto3 = Producto(nombre="Café", precio=5600, descripcion="Águila Roja")
producto4 = Producto(nombre="Gaseosa", precio=1700, descripcion="Postobon")
producto5 = Producto(nombre="Cheetos", precio=6800, descripcion="Doritos")

cliente1.agregar_producto_al_carrito(producto1)
cliente1.agregar_producto_al_carrito(producto2)
cliente1.agregar_producto_al_carrito(producto3)
cliente1.agregar_producto_al_carrito(producto4)
cliente2.agregar_producto_al_carrito(producto5)

cliente1.mostrar_mi_carrito()
cliente1.calcular_valor_productos()
cliente2.mostrar_mi_carrito()
cliente2.calcular_valor_productos()
