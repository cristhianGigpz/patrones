from domain.product import Product


class MemoryProductRepository:
    def __init__(self):
        self.products: dict[int, Product] = {}

    def save(self, product: Product) -> None:

        self.products[product.id] = product

    def find_by_id(self, product_id: int) -> Product | None:

        return self.products.get(product_id)

    def find_all(self) -> list[Product]:

        return list(self.products.values())
