import time
import threading
from concurrent.futures import ThreadPoolExecutor

payment_limit = threading.BoundedSemaphore(3)


# def process_payment(payment_id):
#     time.sleep(1)
#     return f"Pago {payment_id} procesado"
def process_payment(payment_id):
    if not payment_limit.acquire(blocking=False):
        raise RuntimeError("Servicio de pagos ocupado")

    try:
        print(f"Procesando pago {payment_id}")
        time.sleep(2)
        return "Pago completado"

    finally:
        payment_limit.release()


def generate_report(report_id):
    time.sleep(5)
    return f"Reporte {report_id} generado"


payment_pool = ThreadPoolExecutor(max_workers=3)
report_pool = ThreadPoolExecutor(max_workers=2)


try:
    report_futures = [report_pool.submit(generate_report, i) for i in range(1, 6)]

    payment_futures = [payment_pool.submit(process_payment, i) for i in range(1, 4)]

    for future in payment_futures:
        print(future.result())

    for future in report_futures:
        print(future.result())

finally:
    payment_pool.shutdown()
    report_pool.shutdown()
