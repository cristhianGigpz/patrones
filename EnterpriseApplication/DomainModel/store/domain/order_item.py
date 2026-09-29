class OrderItem:
    def __init__(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Cantidad inválida")

        self.product = product
        self.quantity = quantity

    def subtotal(self):

        return self.product.price * self.quantity
