class MessageBus:
    def __init__(self):
        self.handlers = {}

    def subscribe(self, message_type, handler):
        self.handlers.setdefault(message_type, []).append(handler)

    def send(self, message_type, data):
        for handler in self.handlers.get(message_type, []):
            handler(data)


def process_payment(order):
    print(f"Procesando pago: {order['id']}")


def update_inventory(order):
    print(f"Actualizando stock: {order['id']}")


def send_notification(order):
    print(f"Notificando pedido: {order['id']}")


bus = MessageBus()

bus.subscribe("OrderCreated", process_payment)
bus.subscribe("OrderCreated", update_inventory)
bus.subscribe("OrderCreated", send_notification)

order = {"id": 101, "product": "Laptop", "total": 2500}

bus.send("OrderCreated", order)
