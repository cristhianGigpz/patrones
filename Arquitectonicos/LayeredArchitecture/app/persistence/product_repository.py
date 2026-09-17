class ProductRepository:
    def get_product(self, product_id):
        products = {
            1: {"name": "Laptop", "price": 2000},
            2: {"name": "Smartphone", "price": 800},
            3: {"name": "Tablet", "price": 400},
        }

        return products.get(product_id)
