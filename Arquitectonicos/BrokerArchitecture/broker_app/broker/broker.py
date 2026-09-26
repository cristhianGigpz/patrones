class Broker:
    def __init__(self):
        self.services = {}

    def register(self, name, service):
        self.services[name] = service

    def request(self, service_name, operation, *args):
        service = self.services.get(service_name)

        if service is None:
            raise ValueError(f"Servicio '{service_name}' no existe")

        method = getattr(service, operation, None)

        if method is None:
            raise ValueError(f"Operación '{operation}' no existe")

        return method(*args)
