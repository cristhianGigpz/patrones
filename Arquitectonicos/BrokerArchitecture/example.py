class Broker:
    def __init__(self):
        self.services = {}

    def register(self, name, service):
        self.services[name] = service

    def execute(self, name, data):
        service = self.services.get(name)

        if service is None:
            raise ValueError(f"Servicio '{name}' no encontrado")

        return service.execute(data)


class PaymentService:
    def execute(self, data):
        return f"Pago procesado: S/ {data['amount']}"


class NotificationService:
    def execute(self, data):
        return f"Notificación enviada a {data['email']}"


broker = Broker()

broker.register("payment", PaymentService())

broker.register("notification", NotificationService())

result = broker.execute("payment", {"amount": 250})

print(result)
# result = broker.execute("notification", {"email": "soporte@gigpz.com"})
# print(result)
