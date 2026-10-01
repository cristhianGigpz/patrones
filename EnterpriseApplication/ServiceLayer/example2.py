class Product:
    def __init__(self, product_id, name, price, stock):
        self.id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):

        if quantity <= 0:
            raise ValueError("Cantidad inválida")

        if self.stock < quantity:
            raise ValueError("Stock insuficiente")

        self.stock -= quantity

    def find(self, product_id):
        if self.id == product_id:
            return self
        return None


class OrderRepository:
    def __init__(self):
        self.orders = []

    def save(self, order):
        self.orders.append(order)


class OrderService:
    def __init__(self, product_repository, order_repository):
        self.product_repository = product_repository

        self.order_repository = order_repository

    def create_order(self, product_id, quantity):
        product = self.product_repository.find(product_id)

        if product is None:
            raise ValueError("Producto no encontrado")

        product.reduce_stock(quantity)

        order = {
            "product_id": product_id,
            "quantity": quantity,
            "total": product.price * quantity,
        }

        self.order_repository.save(order)

        return order


producto = Product(1, "Laptop", 1000, 10)

service = OrderService(product_repository=producto, order_repository=OrderRepository())

order = service.create_order(1, 2)
print(order)
