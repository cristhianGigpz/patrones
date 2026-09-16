class UserModel:
    def get_user(self):
        return {"name": "Cristhian", "role": "Developer"}


class UserView:
    def show(self, view_model):
        print(f"Nombre: {view_model.name}")
        print(f"Rol: {view_model.role}")


class UserViewModel:
    def __init__(self, model):
        self.model = model
        self.name = ""
        self.role = ""

    def load_user(self):
        user = self.model.get_user()

        self.name = user["name"]
        self.role = user["role"]


model = UserModel()

view_model = UserViewModel(model)
view = UserView()

view_model.load_user()
view.show(view_model)
