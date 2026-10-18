from decimal import Decimal

from sales.domain.product import Product as SalesProduct
from inventory.domain.product import Product as InventoryProduct


sales_product = SalesProduct(id=1, name="Laptop", price=Decimal("3000.00"))

inventory_product = InventoryProduct(id=1, sku="LAP-001", stock=20)

sales_product.apply_discount(10)

inventory_product.remove_stock(2)

print(sales_product.price)
print(inventory_product.stock)
