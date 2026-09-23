import requests

from fastapi import FastAPI, HTTPException

app = FastAPI()


def process_payment(event):
    print(f"Procesando pago del pedido {event['order_id']}")


def send_notification(event):
    print(f"Pedido {event['order_id']} creado")


class EventBus:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event, callback):
        self.listeners.setdefault(event, []).append(callback)

    def publish(self, event, data):
        for callback in self.listeners.get(event, []):
            callback(data)


event_bus = EventBus()
event_bus.subscribe("order_created", process_payment)
event_bus.subscribe("order_created", send_notification)


@app.post("/orders/{product_id}")
def create_order(product_id: int):

    response = requests.get(f"http://localhost:8001/products/{product_id}")

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    product = response.json()
    event_bus.publish("order_created", {"order_id": 101, "total": 250})
    return {"message": "Pedido creado", "product": product}


# uv run uvicorn orders:app --port 8002 --reload
