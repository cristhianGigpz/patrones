from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class OrderConfirmed:
    order_id: int
    occurred_at: datetime


# event = OrderConfirmed(order_id=101, occurred_at=datetime.now(timezone.utc))
# print(event)


class Order:
    def __init__(self, order_id):
        self.id = order_id
        self.status = "pending"
        self._events = []

    def confirm(self):

        if self.status != "pending":
            raise ValueError("El pedido ya fue procesado")

        self.status = "confirmed"

        event = OrderConfirmed(order_id=self.id, occurred_at=datetime.now(timezone.utc))

        self._events.append(event)

    def pull_events(self):
        events = list(self._events)
        self._events.clear()
        return events


class EventBus:
    def __init__(self):
        self.handlers = {}

    def subscribe(self, event_type, handler):
        self.handlers.setdefault(event_type, []).append(handler)

    def publish(self, event):
        for handler in self.handlers.get(type(event), []):
            handler(event)


def send_confirmation_email(event):
    print(f"Enviando correo del pedido {event.order_id}")


def update_statistics(event):
    print(f"Actualizando estadísticas: {event.order_id}")


bus = EventBus()

bus.subscribe(OrderConfirmed, send_confirmation_email)

bus.subscribe(OrderConfirmed, update_statistics)

order = Order(101)

order.confirm()

# events = order.pull_events()
# for event in events:
#     print(event)
for event in order.pull_events():
    bus.publish(event)
