from domain.product import Product

from repositories.product_repository import ProductRepository


class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def create_product(self, product_id: int, name: str, price: float):
        existing = self.repository.find_by_id(product_id)

        if existing:
            raise ValueError("El producto ya existe")

        product = Product(product_id, name, price)

        self.repository.save(product)

        return product

    def get_products(self):

        return self.repository.find_all()
