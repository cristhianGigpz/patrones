class OrderService:
    def create(self):
        print("Pedido creado")

    def cancel(self):
        print("Pedido cancelado")


class InventoryService:
    def reserve(self):
        print("Stock reservado")

    def release(self):
        print("Stock liberado")


class PaymentService:
    def charge(self):
        raise ValueError("Pago rechazado")


class OrderSaga:
    def __init__(self):
        self.orders = OrderService()
        self.inventory = InventoryService()
        self.payments = PaymentService()

    def execute(self):
        compensations = []

        try:
            self.orders.create()
            compensations.append(self.orders.cancel)

            self.inventory.reserve()
            compensations.append(self.inventory.release)

            self.payments.charge()

            print("Compra completada")

        except Exception as error:
            print(f"Error: {error}")

            for compensate in reversed(compensations):
                compensate()


saga = OrderSaga()
saga.execute()
