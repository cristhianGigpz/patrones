from dataclasses import dataclass
from typing import Protocol


# 1. Entity
@dataclass
class Product:
    name: str
    price: float


class ProductRepository(Protocol):
    def get_product(self, product_id: int) -> Product: ...


# 2. Use Case
class GetProduct:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, product_id):
        product = self.repository.get_product(product_id)

        if product is None:
            return None

        return product


class MemoryProductRepository:
    def get_product(self, product_id):
        product = {
            1: {"name": "Laptop", "price": 2000},
            2: {"name": "Teclado", "price": 150},
        }
        return product.get(product_id)


repository = MemoryProductRepository()

get_product = GetProduct(repository)

print(get_product.execute(2))
