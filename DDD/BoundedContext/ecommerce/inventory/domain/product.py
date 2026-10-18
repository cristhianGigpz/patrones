from dataclasses import dataclass


@dataclass
class Product:
    id: int
    sku: str
    stock: int

    def remove_stock(self, quantity):
        if quantity <= 0:
            raise ValueError("Cantidad inválida")

        if quantity > self.stock:
            raise ValueError("Stock insuficiente")

        self.stock -= quantity
