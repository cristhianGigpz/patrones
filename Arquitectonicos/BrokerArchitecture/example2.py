class UserService:
    def get_user(self, user_id):
        return {"id": user_id, "name": "Cristian"}


class ProductService:
    def get_product(self, product_id):
        return {"id": product_id, "name": "Laptop", "price": 2000}


class Broker:
    def __init__(self):
        self.services = {}

    def register(self, name, service):
        self.services[name] = service

    def request(self, service_name, operation, *args):
        service = self.services.get(service_name)

        if service is None:
            raise ValueError("Servicio no encontrado")

        method = getattr(service, operation)

        return method(*args)


broker = Broker()

broker.register("users", UserService())

broker.register("products", ProductService())

user = broker.request("users", "get_user", 1)

product = broker.request("products", "get_product", 10)


print(user)
print(product)
