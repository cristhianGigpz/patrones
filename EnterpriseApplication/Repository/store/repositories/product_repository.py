from typing import Protocol

from domain.product import Product


class ProductRepository(Protocol):
    def save(self, product: Product) -> None: ...

    def find_by_id(self, product_id: int) -> Product | None: ...

    def find_all(self) -> list[Product]: ...
