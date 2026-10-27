class PubSub:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, topic, callback):
        self.subscribers.setdefault(topic, []).append(callback)

    def publish(self, topic, data):
        for callback in self.subscribers.get(topic, []):
            callback(data)


def send_welcome_email(user):
    print(f"Correo enviado a {user['name']}")


def register_activity(user):
    print(f"Actividad registrada: {user['name']}")


def give_reward(user):
    print(f"Bonificación otorgada a {user['name']}")


pubsub = PubSub()

pubsub.subscribe("UserRegistered", send_welcome_email)
pubsub.subscribe("UserRegistered", register_activity)
pubsub.subscribe("UserRegistered", give_reward)

user = {"id": 1, "name": "Ana"}

pubsub.publish("UserRegistered", user)
