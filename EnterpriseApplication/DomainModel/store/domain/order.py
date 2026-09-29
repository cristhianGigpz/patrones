from domain.order_item import OrderItem


class Order:
    def __init__(self, order_id):
        self.id = order_id
        self.items = []
        self.status = "pending"

    def add_product(self, product, quantity):
        if self.status != "pending":
            raise ValueError("El pedido ya no puede modificarse")

        product.reduce_stock(quantity)

        item = OrderItem(product, quantity)

        self.items.append(item)

    def total(self):

        return sum(item.subtotal() for item in self.items)

    def confirm(self):

        if not self.items:
            raise ValueError("El pedido está vacío")

        self.status = "confirmed"
