import queue
import threading
import time

orders = queue.Queue(maxsize=100)


def process_order():
    while True:
        order = orders.get()

        try:
            if order is None:
                break

            print(f"Procesando pedido {order}")
            time.sleep(1)
            print(f"Pedido {order} completado")

        finally:
            orders.task_done()


workers = [threading.Thread(target=process_order) for _ in range(3)]

for worker in workers:
    worker.start()


for order_id in range(1, 11):
    orders.put(order_id)
    print(f"Pedido {order_id} agregado a la cola")

orders.join()

for _ in workers:
    orders.put(None)

for worker in workers:
    worker.join()

print("Todos los pedidos fueron procesados")
