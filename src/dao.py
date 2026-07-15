from src.db import get_connection
from src.modelo import Producto
import sqlite3

class ProductoDAO:
    @staticmethod
    def guardar(producto):
        with get_connection() as conn:
            cursor = conn.cursor()
            if producto.id is None:
                cursor.execute(
                    "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
                    (producto.nombre, producto.precio, producto.stock)
                )
                producto.id = cursor.lastrowid
            else:
                cursor.execute(
                    "UPDATE productos SET nombre=?, precio=?, stock=? WHERE id=?",
                    (producto.nombre, producto.precio, producto.stock, producto.id)
                )
            conn.commit()
            return producto.id

    @staticmethod
    def buscar_por_id(id_producto):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, nombre, precio, stock FROM productos WHERE id = ?",
                (id_producto,)
            )
            fila = cursor.fetchone()
            if fila:
                return Producto(
                    id=fila['id'],
                    nombre=fila['nombre'],
                    precio=fila['precio'],
                    stock=fila['stock']
                )
            return None

    @staticmethod
    def actualizar_stock(id_producto, nuevo_stock):
        with get_connection() as conn:
            try:
                conn.execute(
                    "UPDATE productos SET stock = ? WHERE id = ?",
                    (nuevo_stock, id_producto)
                )
                conn.commit()
            except sqlite3.Error as e:
                conn.rollback()
                raise RuntimeError(f"Error al actualizar stock: {e}")
              
