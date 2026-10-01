from models.product import Product


class ProductService:
    def __init__(self, repository):
        self.repository = repository

    def create_product(self, product_id, name, price):
        if price <= 0:
            raise ValueError("El precio debe ser mayor a 0")

        product = Product(product_id, name, price)

        self.repository.save(product)

        return product

    def get_product(self, product_id):

        product = self.repository.find(product_id)

        if product is None:
            raise ValueError("Producto no encontrado")

        return product
