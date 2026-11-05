import json
import redis

database = {
    1: {"name": "Laptop", "price": 2500},
    2: {"name": "Mouse", "price": 80},
}

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)


def get_product(product_id):
    key = f"product:{product_id}"

    # Buscar en Redis
    cached = redis_client.get(key)

    if cached is not None:
        print("Cache Hit")
        return json.loads(cached)

    # Consultar base de datos
    print("Cache Miss")
    product = database.get(product_id)

    if product is None:
        return None

    # Guardar durante 60 segundos
    redis_client.set(key, json.dumps(product), ex=60)

    return product


# redis_client.delete(f"product:{product_id}")
print(get_product(1))
print(get_product(1))
