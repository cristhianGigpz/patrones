import requests


def create_order(product_id: int):

    response = requests.get(f"http://localhost:8001/products/{product_id}")

    if response.status_code != 200:
        return None

    product = response.json()

    return {"id": 101, "product": product, "status": "created"}
