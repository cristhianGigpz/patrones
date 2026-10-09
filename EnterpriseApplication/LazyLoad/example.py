class Customer:
    def __init__(self, customer_id, name, order_repository):
        self.id = customer_id
        self.name = name

        self.order_repository = order_repository
        self._orders = None

    @property
    def orders(self):

        if self._orders is None:
            print("Cargando pedidos...")

            self._orders = self.order_repository.find_by_customer(self.id)

        return self._orders


class OrderRepository:
    def find_by_customer(self, customer_id):

        return [{"id": 1, "total": 200}, {"id": 2, "total": 500}]


repository = OrderRepository()

customer = Customer(customer_id=1, name="Carlos", order_repository=repository)

print(customer.name)

print(customer.orders)
print(customer.orders)
