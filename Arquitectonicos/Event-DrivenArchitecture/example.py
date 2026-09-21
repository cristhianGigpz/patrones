class EventBus:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event, callback):
        self.listeners.setdefault(event, []).append(callback)

    def publish(self, event, data):
        for callback in self.listeners.get(event, []):
            callback(data)


def send_welcome_email(user):
    print(f"Bienvenido, {user['name']}!")


class UserService:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def register(self, name):
        user = {"name": name}

        print("Usuario registrado")

        self.event_bus.publish("user_registered", user)


event_bus = EventBus()

event_bus.subscribe("user_registered", send_welcome_email)

service = UserService(event_bus)

service.register("Cristian")
