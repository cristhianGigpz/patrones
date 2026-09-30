class ProductTable:
    def __init__(self, products):
        self.products = products

    def get(self, product_id):
        return self.products.get(product_id)

    def reduce_stock(self, product_id, quantity):
        product = self.get(product_id)

        if product is None:
            raise ValueError("Producto no encontrado")

        if quantity <= 0:
            raise ValueError("Cantidad inválida")

        if product["stock"] < quantity:
            raise ValueError("Stock insuficiente")

        product["stock"] -= quantity
