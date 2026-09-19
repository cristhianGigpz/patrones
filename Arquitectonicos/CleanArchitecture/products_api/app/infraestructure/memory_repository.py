from app.entities.product import Product


class MemoryProductRepository:
    def __init__(self):
        self.products = {1: Product("Laptop", 2000), 2: Product("Mouse", 100)}

    def get_product(self, product_id: int):
        return self.products.get(product_id)
