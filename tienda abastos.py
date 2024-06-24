# tienda de abastos sr. Marco
# realizar en base de POO
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} ({self.cantidad} unidades)"


class TiendaAbastos:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = []

    def agregar_producto(self, producto):
        self.inventario.append(producto)

    def mostrar_inventario(self):
        print(f"Inventario de la tienda '{self.nombre}':")
        for producto in self.inventario:
            print(producto)

    def calcular_valor_total(self):
        total = sum(producto.precio * producto.cantidad for producto in self.inventario)
        return total


# Ejemplo de uso
def main():
    # Crear algunos productos
    producto1 = Producto("Arroz", 2.5, 10)
    producto2 = Producto("Frijoles", 3.0, 8)
    producto3 = Producto("Aceite", 5.0, 5)

    # Crear una tienda de abastos
    tienda = TiendaAbastos("Supermercado Don Pepe")

    # Agregar productos al inventario de la tienda
    tienda.agregar_producto(producto1)
    tienda.agregar_producto(producto2)
    tienda.agregar_producto(producto3)

    # Mostrar el inventario de la tienda
    tienda.mostrar_inventario()

    # Calcular el valor total del inventario en la tienda
    total = tienda.calcular_valor_total()
    print(f"\nValor total del inventario: ${total:.2f}")