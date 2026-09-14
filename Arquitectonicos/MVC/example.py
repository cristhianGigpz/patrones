class UserModel:
    def get_user(self):
        return {"name": "Cristian", "role": "Developer"}

    def find(self, user_id):
        # Simulación de búsqueda de usuario por ID
        if user_id == 1:
            return {"name": "Cristian", "role": "Developer"}
        elif user_id == 2:
            return {"name": "Ana", "role": "Designer"}
        else:
            return {"name": "Desconocido", "role": "Invitado"}


class UserView:
    def show_user(self, user):
        print(f"Nombre: {user['name']}")
        print(f"Rol: {user['role']}")

    def render(self, user):
        return f"Nombre: {user['name']}, Rol: {user['role']}"


class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_user(self):
        user = self.model.get_user()

        self.view.show_user(user)

    def get_user(self, user_id):
        user = self.model.find(user_id)
        return self.view.render(user)


model = UserModel()
view = UserView()

controller = UserController(model, view)

controller.show_user()

# user = {"name": "Cristian", "role": "Developer"}

# name = user["name"].upper()

# print(f"Usuario: {name}")
# print(f"Rol: {user['role']}")
print("------------------------")
user_id = 2
user_info = controller.get_user(user_id)
print(user_info)
