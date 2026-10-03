class Product:
    def __init__(self, product_id, name, price):
        self.id = product_id
        self.name = name
        self.price = price


row = {"id": 1, "name": "Laptop", "price": 2000}


class ProductMapper:
    def to_domain(self, row):

        return Product(product_id=row["id"], name=row["name"], price=row["price"])

    def to_data(self, product):

        return {"id": product.id, "name": product.name, "price": product.price}


mapper = ProductMapper()

product = mapper.to_domain(row)

print(product.name)
print(product.price)

data = mapper.to_data(product)

print(data)
