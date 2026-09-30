from database.data import products, orders

from modules.product_table import ProductTable

from modules.order_table import OrderTable


product_table = ProductTable(products)

order_table = OrderTable(orders, product_table)


order = order_table.create(order_id=101, product_id=1, quantity=2)

print(order)
