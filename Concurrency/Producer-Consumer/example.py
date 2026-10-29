import threading
import queue
import time

tasks = queue.Queue()
# tasks = queue.Queue(maxsize=100)


def producer():
    for i in range(1, 6):
        task = f"Imagen {i}"

        tasks.put(task)

        print(f"Producida: {task}")
        time.sleep(0.2)


def consumer():
    while True:
        task = tasks.get()

        if task is None:
            tasks.task_done()
            break

        try:
            print(f"Procesando: {task}")
            time.sleep(0.5)
            print(f"Completada: {task}")
        finally:
            tasks.task_done()


producer_thread = threading.Thread(target=producer)

# consumer_thread = threading.Thread(target=consumer)
consumers = [threading.Thread(target=consumer) for _ in range(3)]

for thread in consumers:
    thread.start()
# consumer_thread.start()

producer_thread.start()

producer_thread.join()

# tasks.put(None)
for _ in consumers:
    tasks.put(None)


tasks.join()

# consumer_thread.join()
for thread in consumers:
    thread.join()


print("Todas las tareas finalizadas")
