class OrderTable:
    def __init__(self, orders, product_table):
        self.orders = orders
        self.product_table = product_table

    def create(self, order_id, product_id, quantity):
        product = self.product_table.get(product_id)

        if product is None:
            raise ValueError("Producto no encontrado")

        self.product_table.reduce_stock(product_id, quantity)

        total = product["price"] * quantity

        order = {
            "id": order_id,
            "product_id": product_id,
            "quantity": quantity,
            "total": total,
        }

        self.orders[order_id] = order

        return order
