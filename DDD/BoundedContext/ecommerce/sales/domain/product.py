from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Product:
    id: int
    name: str
    price: Decimal

    def apply_discount(self, percentage):
        if not 0 <= percentage <= 100:
            raise ValueError("Descuento inválido")

        discount = self.price * (Decimal(str(percentage)) / 100)

        self.price -= discount
