from domain.product import Product
from domain.order import Order

from repositories.order_repository import OrderRepository


laptop = Product(product_id=1, name="Laptop", price=2000, stock=5)

mouse = Product(product_id=2, name="Mouse", price=100, stock=10)


order = Order(order_id=101)

order.add_product(laptop, 1)
order.add_product(mouse, 2)

print(order.total())

order.confirm()


repository = OrderRepository()

repository.save(order)
