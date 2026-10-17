from dataclasses import dataclass
from decimal import Decimal
from uuid import uuid4


@dataclass(frozen=True)
class OrderItem:
    product_id: int
    quantity: int
    price: Decimal

    def __post_init__(self):
        if self.quantity <= 0:
            raise ValueError("Cantidad inválida")

        if self.price < 0:
            raise ValueError("Precio inválido")


class Order:
    def __init__(self, order_id, customer_id, items):
        self.id = order_id
        self.customer_id = customer_id
        self._items = tuple(items)
        self._status = "pending"

    @property
    def items(self):
        return self._items

    @property
    def status(self):
        return self._status

    def total(self):
        return sum(
            (item.price * item.quantity for item in self._items), Decimal("0.00")
        )


class OrderFactory:
    @staticmethod
    def create(customer_id, items):

        if customer_id <= 0:
            raise ValueError("Cliente inválido")

        if not items:
            raise ValueError("El pedido necesita productos")

        if not all(isinstance(item, OrderItem) for item in items):
            raise ValueError("Los elementos deben ser OrderItem")

        return Order(order_id=str(uuid4()), customer_id=customer_id, items=items)


items = [
    OrderItem(product_id=1, quantity=2, price=Decimal("100.00")),
    OrderItem(product_id=2, quantity=1, price=Decimal("50.00")),
]

order = OrderFactory.create(customer_id=5, items=items)

print(order.status)
print(order.total())
