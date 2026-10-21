import time


class CircuitBreaker:
    def __init__(self, max_failures=3, timeout=5):
        self.max_failures = max_failures
        self.timeout = timeout

        self.failures = 0
        self.state = "CLOSED"
        self.last_failure = 0

    def execute(self, operation):

        if self.state == "OPEN":
            elapsed = time.monotonic() - self.last_failure

            if elapsed < self.timeout:
                print(elapsed)
                raise RuntimeError("Circuito abierto: servicio no disponible")

            self.state = "HALF-OPEN"

        try:
            result = operation()

            self.failures = 0
            self.state = "CLOSED"

            return result

        except Exception:
            self.failures += 1
            self.last_failure = time.monotonic()

            if self.state == "HALF-OPEN" or self.failures >= self.max_failures:
                self.state = "OPEN"

            raise


def payment_service():
    raise ConnectionError("No se puede conectar al servicio de pagos")


breaker = CircuitBreaker(max_failures=3, timeout=5)

for attempt in range(5):
    try:
        breaker.execute(payment_service)

    except Exception as error:
        print(f"Intento {attempt + 1}: {error}")

    print("Estado:", breaker.state)
