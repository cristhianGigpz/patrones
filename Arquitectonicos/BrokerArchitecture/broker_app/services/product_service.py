class ProductService:
    def __init__(self):
        self.products = {
            1: {"name": "Laptop", "price": 2000},
            2: {"name": "Mouse", "price": 100},
        }

    def get_product(self, product_id):
        return self.products.get(product_id)
