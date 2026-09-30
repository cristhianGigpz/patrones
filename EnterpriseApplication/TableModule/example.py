"""
products
┌────┬──────────┬───────┬───────┐
│ id │ name     │ price │ stock │
├────┼──────────┼───────┼───────┤
│ 1  │ Laptop   │ 2000  │ 5     │
│ 2  │ Mouse    │ 100   │ 10    │
└────┴──────────┴───────┴───────┘
"""

products = {
    1: {"name": "Laptop", "price": 2000, "stock": 5},
    2: {"name": "Mouse", "price": 100, "stock": 10},
}


class ProductTable:
    def __init__(self, products):
        self.products = products

    def get(self, product_id):
        return self.products.get(product_id)

    def calculate_discount(self, product_id, percentage):
        product = self.get(product_id)

        if product is None:
            raise ValueError("Producto no encontrado")

        discount = product["price"] * percentage / 100

        return product["price"] - discount


table = ProductTable(products)

price = table.calculate_discount(product_id=1, percentage=10)

print(price)
