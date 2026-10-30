import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed


def process_task(task_id):
    thread_name = threading.current_thread().name

    print(f"Tarea {task_id} iniciada en {thread_name}")

    time.sleep(2)

    return f"Tarea {task_id} completada"


# with ThreadPoolExecutor(max_workers=3) as executor:
#     results = executor.map(process_task, range(1, 7))

#     for result in results:
#         print(result)

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(process_task, i) for i in range(1, 7)]

    for future in as_completed(futures):
        print(future.result())
