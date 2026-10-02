# class ProductService:

#     def get_product(self, product_id):
#         cursor.execute(
#             """
#             SELECT id, name, price
#             FROM products
#             WHERE id = %s
#             """,
#             (product_id,)
#         )

#         return cursor.fetchone()


class Product:
    def __init__(self, product_id, name, price):
        self.id = product_id
        self.name = name
        self.price = price


class ProductRepository:
    def __init__(self):
        self.products = {}

    def save(self, product):
        self.products[product.id] = product

    def find_by_id(self, product_id):
        return self.products.get(product_id)

    def find_all(self):
        return list(self.products.values())

    def delete(self, product_id):
        self.products.pop(product_id, None)


repository = ProductRepository()

product = Product(1, "Laptop", 2000)

repository.save(product)

result = repository.find_by_id(1)

print(result.name)
