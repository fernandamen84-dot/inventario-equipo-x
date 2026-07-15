class StockInsuficienteError(Exception):
    def __init__(self, mensaje, stock_disponible=None, cantidad_solicitada=None):
        self.stock_disponible = stock_disponible
        self.cantidad_solicitada = cantidad_solicitada
        super().__init__(mensaje)

class ProductoNoEncontradoError(Exception):
    pass
