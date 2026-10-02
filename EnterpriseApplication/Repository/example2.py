from typing import Protocol


class Product:
    def __init__(self, product_id, name, price):
        self.id = product_id
        self.name = name
        self.price = price


class ProductRepository(Protocol):
    def save(self, product): ...

    def find_by_id(self, product_id): ...

    def find_all(self): ...


class MemoryProductRepository:
    def __init__(self):
        self.products = {}

    def save(self, product):
        self.products[product.id] = product

    def find_by_id(self, product_id):
        return self.products.get(product_id)

    def find_all(self):
        return list(self.products.values())


class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def get_product(self, product_id):

        product = self.repository.find_by_id(product_id)

        if product is None:
            raise ValueError("Producto no encontrado")

        return product

    def save_product(self, product):
        self.repository.save(product)


repository = MemoryProductRepository()

service = ProductService(repository)
service.save_product(Product(1, "Laptop", 2000))

product = service.get_product(1)
print(product.name)
