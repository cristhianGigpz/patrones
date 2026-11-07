import time
from collections import defaultdict, deque

requests = defaultdict(deque)

LIMIT = 3  # Máximo de solicitudes permitidas
WINDOW = 10  # Tamaño de la ventana de tiempo en segundos


def allow_request(user_id):
    now = time.monotonic()
    user_requests = requests[user_id]

    # Eliminar solicitudes fuera de la ventana
    while user_requests and now - user_requests[0] >= WINDOW:
        user_requests.popleft()

    # Comprobar límite
    if len(user_requests) >= LIMIT:
        return False

    user_requests.append(now)
    return True


for i in range(5):
    if allow_request("user_123"):
        print(f"Solicitud {i + 1}: permitida")
    else:
        print(f"Solicitud {i + 1}: rechazada")
