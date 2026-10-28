def process_card(message):
    print(f"Pago con tarjeta: S/ {message['amount']}")


def process_paypal(message):
    print(f"Pago con PayPal: S/ {message['amount']}")


def process_bank(message):
    print(f"Transferencia bancaria: S/ {message['amount']}")


class MessageRouter:
    def __init__(self):
        self.routes = {}

    def register(self, message_type, handler):
        self.routes[message_type] = handler

    def route(self, message):
        message_type = message.get("payment_method")

        handler = self.routes.get(message_type)

        if handler is None:
            raise ValueError("Método de pago no soportado")

        return handler(message)


router = MessageRouter()

router.register("card", process_card)
router.register("paypal", process_paypal)
router.register("bank", process_bank)

payments = [
    {"payment_method": "card", "amount": 150},
    {"payment_method": "paypal", "amount": 200},
    {"payment_method": "bank", "amount": 350},
]

for payment in payments:
    router.route(payment)
