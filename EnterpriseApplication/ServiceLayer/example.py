class UserRepository:
    def __init__(self):
        self.users = {}

    def save(self, user):
        self.users[user["id"]] = user

    def find(self, user_id):
        return self.users.get(user_id)


class UserService:
    def __init__(self, repository):
        self.repository = repository

    def register(self, user_id, name):

        if not name.strip():
            raise ValueError("Nombre obligatorio")

        user = {"id": user_id, "name": name}

        self.repository.save(user)

        return user

    def get_user(self, user_id):

        user = self.repository.find(user_id)

        if user is None:
            raise ValueError("Usuario no encontrado")

        return user


repository = UserRepository()

service = UserService(repository)

# user = service.register(1, "Cristian")
# print(user)
service.register(1, "Cristian")
print(service.get_user(1))
