from dataclasses import dataclass
from decimal import Decimal


class OrderRepository:
    def find_by_id(self, order_id): ...

    def save(self, order): ...


class OrderService:
    def __init__(self, repository):
        self.repository = repository

    def confirm_order(self, order_id):

        order = self.repository.find_by_id(order_id)

        if order is None:
            raise ValueError("Pedido no encontrado")

        order.confirm()

        self.repository.save(order)


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
        return self.quantity * self.price


class Order:
    def __init__(self, order_id):
        self.id = order_id
        self._status = "pending"
        self._items = []

    @property
    def status(self):
        return self._status

    @property
    def items(self):
        return tuple(self._items)

    def add_item(self, product_id, quantity, price):
        if self._status != "pending":
            raise ValueError("El pedido no se puede modificar")

        item = OrderItem(product_id, quantity, price)

        self._items.append(item)

    def total(self):
        return sum((item.subtotal() for item in self._items), Decimal("0.00"))

    def confirm(self):
        if self._status != "pending":
            raise ValueError("El pedido ya fue procesado")

        if not self._items:
            raise ValueError("No se puede confirmar un pedido vacío")

        self._status = "confirmed"

    def change_quantity(self, product_id, quantity):

        if self._status != "pending":
            raise ValueError("No se puede modificar el pedido")

        if quantity <= 0:
            raise ValueError("Cantidad inválida")

        for index, item in enumerate(self._items):
            if item.product_id == product_id:
                self._items[index] = OrderItem(
                    product_id=item.product_id, quantity=quantity, price=item.price
                )

                return

        raise ValueError("Producto no encontrado")


order = Order(order_id=101)

order.add_item(product_id=1, quantity=2, price=Decimal("100.00"))

order.add_item(product_id=2, quantity=1, price=Decimal("50.00"))

print(order.total())

order.change_quantity(product_id=1, quantity=5)

print(order.total())

order.confirm()
print(order.status)

# order.add_item(product_id=3, quantity=1, price=Decimal("20.00"))

# order.items[0].quantity = 5
