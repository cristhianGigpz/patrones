from typing import Protocol

from ..domain.product import Product


class ProductRepository(Protocol):
    def get_product(self, product_id: int) -> Product | None: ...
