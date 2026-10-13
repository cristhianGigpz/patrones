from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class OrderItem:
    product_id: int
    quantity: int
    price: Decimal

    def __post_init__(self):
        if self.quantity <= 0:
            raise ValueError("La cantidad debe ser positiva")

        if self.price < 0:
            raise ValueError("El precio no puede ser negativo")

    def subtotal(self):
        return self.price * self.quantity


class Order:
    def __init__(self, order_id):
        self.id = order_id
        self.status = "pending"
        self._items = []

    @property
    def items(self):
        return tuple(self._items)

    def add_item(self, product_id, quantity, price):
        if self.status != "pending":
            raise ValueError("No se puede modificar el pedido")

        item = OrderItem(product_id, quantity, price)

        self._items.append(item)

    def total(self):
        return sum((item.subtotal() for item in self._items), Decimal("0.00"))

    def confirm(self):
        if not self._items:
            raise ValueError("No se puede confirmar un pedido vacío")

        if self.status != "pending":
            raise ValueError("El pedido ya fue procesado")

        self.status = "confirmed"


order = Order(order_id=101)

order.add_item(product_id=1, quantity=2, price=Decimal("100.00"))

order.add_item(product_id=2, quantity=1, price=Decimal("200.00"))

print(order.total())

order.confirm()

print(order.status)

order.add_item(product_id=3, quantity=1, price=Decimal("50.00"))
