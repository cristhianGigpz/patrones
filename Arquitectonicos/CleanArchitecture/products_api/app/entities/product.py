from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float

    def apply_discount(self):
        return self.price * 0.90
