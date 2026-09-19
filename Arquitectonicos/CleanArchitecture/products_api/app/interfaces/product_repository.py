from typing import Protocol

from app.entities.product import Product


class ProductRepository(Protocol):
    def get_product(self, product_id: int) -> Product | None: ...
