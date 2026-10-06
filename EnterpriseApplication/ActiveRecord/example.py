class Product:
    database = {}

    def __init__(self, product_id, name, price):
        self.id = product_id
        self.name = name
        self.price = price

    def save(self):
        Product.database[self.id] = self

    def delete(self):
        Product.database.pop(self.id, None)

    @classmethod
    def find(cls, product_id):
        return cls.database.get(product_id)


product = Product(1, "Laptop", 2000)

product.save()

productId = Product.find(1)

print(productId.name)

product.delete()
productId = Product.find(1)
print(productId)
