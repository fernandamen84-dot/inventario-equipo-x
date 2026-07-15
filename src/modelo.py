class Producto:
    """Clase Producto con encapsulacion usando @property"""

    def __init__(self, nombre, precio, stock, id=None):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        self._precio = valor

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise ValueError("El stock no puede ser negativo")
        self._stock = valor

    def __repr__(self):
        return f"Producto(id={self.id}, nombre='{self.nombre}', precio={self.precio}, stock={self.stock})"
