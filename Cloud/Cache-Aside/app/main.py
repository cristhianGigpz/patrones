import json
import time
import redis

# 1. Base de datos simulada
database = {
    1: {"name": "Laptop", "price": 2500},
    2: {"name": "Mouse", "price": 80},
}

# 2. Conexión a Redis
# decode_responses=True convierte automáticamente los bytes de Redis a strings de Python
redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)


def get_product(product_id):
    key = f"product:{product_id}"

    try:
        # Buscar en Redis
        cached = redis_client.get(key)

        if cached is not None:
            print(" Visualizando: [Cache Hit] - Traído desde Redis")
            return json.loads(cached)

        # Consultar base de datos
        print(" Visualizando: [Cache Miss] - Buscando en Base de Datos")
        product = database.get(product_id)

        if product is None:
            return None

        # Guardar en Redis usando .set con el parámetro ex
        # Reemplaza a: redis_client.setex(key, 60, json.dumps(product))
        redis_client.set(key, json.dumps(product), ex=60)

        return product

    except redis.exceptions.ConnectionError:
        print(
            "❌ Error: No se pudo conectar a Redis. Asegúrate de que el servidor está corriendo."
        )
        return database.get(product_id)


# --- PRUEBAS DE EJECUCIÓN ---
if __name__ == "__main__":
    # Limpiamos las llaves de prueba en Redis para empezar desde cero
    try:
        redis_client.delete("product:1", "product:2")
        print("🧹 Redis limpio para la simulación.\n" + "-" * 50)
    except redis.exceptions.ConnectionError:
        pass

    # Primera consulta: Debe ser Cache Miss (va a la DB)
    print("--- Primera consulta del Producto 1 ---")
    p1 = get_product(1)
    print(f"Resultado: {p1}\n")

    # Segunda consulta: Debe ser Cache Hit (va a Redis)
    print("--- Segunda consulta del Producto 1 (Inmediata) ---")
    p2 = get_product(1)
    print(f"Resultado: {p2}\n")

    # Tercera consulta: Producto diferente (Cache Miss)
    print("--- Primera consulta del Producto 2 ---")
    p3 = get_product(2)
    print(f"Resultado: {p3}\n")

    # Cuarta consulta: Producto que NO existe
    print("--- Consulta de un producto inexistente (ID 99) ---")
    p99 = get_product(99)
    print(f"Resultado: {p99}\n")
