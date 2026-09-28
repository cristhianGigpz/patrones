from repositories.product_repository import find_product

from repositories.order_repository import save_order


def create_order(product_id, quantity):

    product = find_product(product_id)

    if product is None:
        raise ValueError("Producto no encontrado")

    if product["stock"] < quantity:
        raise ValueError("Stock insuficiente")

    total = product["price"] * quantity

    order = {"product_id": product_id, "quantity": quantity, "total": total}

    product["stock"] -= quantity

    save_order(order)

    return order
