from repositories.memory_product_repository import MemoryProductRepository

from services.product_service import ProductService


repository = MemoryProductRepository()

service = ProductService(repository)


service.create_product(1, "Laptop", 2000)

service.create_product(2, "Mouse", 100)


products = service.get_products()

for product in products:
    print(product.name, product.price)
