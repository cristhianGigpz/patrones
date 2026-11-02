import random
import time
from unittest import result


class TemporaryError(Exception):
    pass


def external_service():
    if random.random() < 0.7:
        raise TemporaryError("Servicio no disponible")

    return {"status": "success"}


def retry(operation, max_attempts=4):
    for attempt in range(1, max_attempts + 1):
        try:
            return operation()

        except TemporaryError as error:
            print(f"Intento {attempt}: {error}")

            if attempt == max_attempts:
                raise

            delay = 2 ** (attempt - 1)

            print(f"Reintentando en {delay}s...")
            time.sleep(delay)


def retry_with_jitter(operation, max_attempts=4):
    for attempt in range(max_attempts):
        try:
            return operation()

        except TemporaryError as error:
            print(f"Intento {attempt}: {error}")
            if attempt == max_attempts - 1:
                raise

            max_delay = min(2**attempt, 30)
            delay = random.uniform(0, max_delay)

            time.sleep(delay)


try:
    # result = retry(external_service)
    result = retry_with_jitter(external_service)
    print("Resultado:", result)

except TemporaryError:
    print("No se pudo completar la operación")
