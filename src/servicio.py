from src.dao import ProductoDAO
from src.modelo import Producto
from src.excepciones import StockInsuficienteError, ProductoNoEncontradoError

class InventarioService:
    @staticmethod
    def vender(id_producto, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser positiva")

        producto = ProductoDAO.buscar_por_id(id_producto)
        if not producto:
            raise ProductoNoEncontradoError(f"Producto con ID {id_producto} no existe")

        if producto.stock < cantidad:
            raise StockInsuficienteError(
                f"Stock insuficiente. Disponible: {producto.stock}, Solicitado: {cantidad}",
                stock_disponible=producto.stock,
                cantidad_solicitada=cantidad
            )

        nuevo_stock = producto.stock - cantidad
        ProductoDAO.actualizar_stock(id_producto, nuevo_stock)

        return {
            'producto': producto.nombre,
            'vendido': cantidad,
            'stock_restante': nuevo_stock
        }
