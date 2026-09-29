class Product:
    def __init__(self, product_id, name, price, stock):
        self.id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):

        if quantity <= 0:
            raise ValueError("Cantidad inválida")

        if quantity > self.stock:
            raise ValueError("Stock insuficiente")

        self.stock -= quantity
