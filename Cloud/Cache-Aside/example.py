database = {
    1: {"name": "Laptop", "price": 2500},
    2: {"name": "Mouse", "price": 80},
}

cache: dict[int, dict[str, str | int]] = {}


def get_product(product_id):

    # 1. Buscar en caché
    if product_id in cache:
        print("Cache Hit")
        return cache[product_id].copy()

    # 2. Consultar base de datos
    print("Cache Miss")

    product = database.get(product_id)

    if product is None:
        return None

    # 3. Guardar en caché
    cache[product_id] = product.copy()

    return product.copy()


def update_product(product_id, price):

    product = database.get(product_id)

    if product is None:
        return False

    # Actualizar base de datos
    database[product_id] = {**product, "price": price}

    # Invalidar caché
    cache.pop(product_id, None)

    return True


print(get_product(1))
print(get_product(1))
print(update_product(1, 2600))
print(get_product(1))
print(get_product(1))
print(get_product(2))
