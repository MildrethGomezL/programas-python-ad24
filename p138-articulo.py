#TAREA 9

import os  

class Producto:
    # Atributos de la clase Producto
    def __init__(self, codigo, descripcion, cantidad_stock, precio_unitario):
        self.codigo = codigo                  
        self.descripcion = descripcion        
        self.cantidad_stock = cantidad_stock  
        self.precio_unitario = precio_unitario 


    def obtener_total(self):
        return self.precio_unitario * self.cantidad_stock

    # Método para convertir la información del producto en una cadena de texto legible
    def __str__(self):
        return (f"Código = {self.codigo}, Descripción = {self.descripcion}, "
                f"Cantidad en stock = {self.cantidad_stock}, Precio unitario = {self.precio_unitario}, "
                f"Total = {self.obtener_total():.2f}")

os.system("cls")  


producto1 = Producto('A101', 'Pluma Roja', 888, 0.08)
print(producto1)  

# Cantidad en stock 
producto1.cantidad_stock = 999
producto1.precio_unitario = 0.99

# valores actualizados de los atributos 
print("Código         =", producto1.codigo)
print("Descripción    =", producto1.descripcion)
print("Cantidad stock =", producto1.cantidad_stock)
print("Precio unitario=", producto1.precio_unitario)
print("Total          =", producto1.obtener_total())  # Imprime el total calculado de producto1


producto2 = Producto("A102", "Pluma Azul", 934, 1.2)
print(producto2)

producto3 = Producto("P103", "Lápiz del 12", 456, 0.5)
print(producto3)

# Total
total_general = producto1.obtener_total() + producto2.obtener_total() + producto3.obtener_total()
print('Total de todos los productos:', total_general)
