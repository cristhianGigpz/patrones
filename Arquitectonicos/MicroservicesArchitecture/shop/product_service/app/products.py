products = {1: {"name": "Laptop", "price": 2000}, 2: {"name": "Mouse", "price": 100}}


def find_product(product_id: int):
    return products.get(product_id)
