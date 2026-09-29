class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):

        if quantity <= 0:
            raise ValueError("Cantidad inválida")

        if quantity > self.stock:
            raise ValueError("Stock insuficiente")

        self.stock -= quantity


class Order:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        product.reduce_stock(quantity)

        self.items.append({"product": product, "quantity": quantity})

    def calculate_total(self):

        return sum(item["product"].price * item["quantity"] for item in self.items)


laptop = Product("Laptop", 2000, 5)

mouse = Product("Mouse", 100, 10)

order = Order()

order.add_product(laptop, 1)
order.add_product(mouse, 2)

print(order.calculate_total())
