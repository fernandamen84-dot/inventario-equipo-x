import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.modelo import Producto
from src.dao import ProductoDAO
from src.servicio import InventarioService
from src.excepciones import StockInsuficienteError
from src.db import init_db, get_connection

class TestProducto(unittest.TestCase):

    def setUp(self):
        init_db()
        with get_connection() as conn:
            conn.execute("DELETE FROM productos")
            conn.commit()

    def test_crear_producto_valido(self):
        producto = Producto("Laptop", 1500.00, 10)
        self.assertEqual(producto.nombre, "Laptop")
        self.assertEqual(producto.precio, 1500.00)
        self.assertEqual(producto.stock, 10)

    def test_precio_negativo(self):
        with self.assertRaises(ValueError):
            Producto("Mouse", -50, 5)

    def test_stock_negativo(self):
        with self.assertRaises(ValueError):
            Producto("Teclado", 50, -5)

    def test_vender_exitoso(self):
        producto = Producto("Mouse", 25, 5)
        id_producto = ProductoDAO.guardar(producto)
        resultado = InventarioService.vender(id_producto, 2)
        self.assertEqual(resultado['vendido'], 2)
        self.assertEqual(resultado['stock_restante'], 3)

    def test_vender_sin_stock(self):
        producto = Producto("Monitor", 300, 3)
        id_producto = ProductoDAO.guardar(producto)
        with self.assertRaises(StockInsuficienteError):
            InventarioService.vender(id_producto, 10)

if __name__ == "__main__":
    unittest.main()
