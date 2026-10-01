class ProductRepository:
    def __init__(self):
        self.products = {}

    def save(self, product):
        self.products[product.id] = product

    def find(self, product_id):
        return self.products.get(product_id)
