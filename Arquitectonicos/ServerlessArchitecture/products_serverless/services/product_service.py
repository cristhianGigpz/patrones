products = {1: {"name": "Laptop", "price": 2000}}


def find_product(product_id):
    return products.get(product_id)


def save_product(product):
    product_id = len(products) + 1

    products[product_id] = product

    return {"id": product_id, **product}


"""
users = []


def create_user(user):
    users.append(user)
"""
