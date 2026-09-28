products = {
    1: {"name": "Laptop", "price": 2000, "stock": 5},
    2: {"name": "Mouse", "price": 150, "stock": 3},
}


def find_product(product_id):
    return products.get(product_id)
