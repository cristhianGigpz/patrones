class EventBus:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event, callback):
        self.listeners.setdefault(event, []).append(callback)

    def publish(self, event, data):
        for callback in self.listeners.get(event, []):
            callback(data)


def send_confirmation(order):
    print(f"Confirmación enviada: {order['id']}")


def update_statistics(order):
    print(f"Venta registrada: S/ {order['total']}")


class OrderService:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def create_order(self, order):
        print("Compra realizada")

        self.event_bus.publish("order_created", order)


event_bus = EventBus()

event_bus.subscribe("order_created", send_confirmation)

event_bus.subscribe("order_created", update_statistics)

service = OrderService(event_bus)

service.create_order({"id": 101, "total": 250})
