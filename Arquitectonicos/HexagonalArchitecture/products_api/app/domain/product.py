from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float

    def discounted_price(self):
        return self.price * 0.90
