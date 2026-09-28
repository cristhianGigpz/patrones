products = {1: {"name": "Laptop", "price": 2000, "stock": 5}}
orders = []


def create_order(product_id, quantity):

    product = products.get(product_id)

    if product is None:
        raise ValueError("Producto no encontrado")

    if quantity <= 0:
        raise ValueError("Cantidad inválida")

    if product["stock"] < quantity:
        raise ValueError("Stock insuficiente")

    total = product["price"] * quantity

    order = {"product_id": product_id, "quantity": quantity, "total": total}

    product["stock"] -= quantity

    orders.append(order)

    return order


order = create_order(1, 2)

print(order)
