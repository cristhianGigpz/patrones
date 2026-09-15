class UserModel:
    def get_user(self):
        return {"name": "Cristhian", "role": "Developer"}


class UserView:
    def show_user(self, name, role):
        print(f"Nombre: {name}")
        print(f"Rol: {role}")


class UserPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def load_user(self):
        user = self.model.get_user()
        name = user["name"].upper()
        self.view.show_user(name, user["role"])


model = UserModel()
view = UserView()

presenter = UserPresenter(model, view)
presenter.load_user()
