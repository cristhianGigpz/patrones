class LoginModel:
    def authenticate(self, username, password):
        return username == "admin" and password == "1234"


class LoginView:
    def show_success(self):
        print("Inicio de sesión correcto")

    def show_error(self):
        print("Usuario o contraseña incorrectos")


class LoginPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def login(self, username, password):

        authenticated = self.model.authenticate(username, password)

        if authenticated:
            self.view.show_success()
        else:
            self.view.show_error()


model = LoginModel()
view = LoginView()

presenter = LoginPresenter(model, view)

presenter.login("admin", "1234")

# user = database.get_user()

# if user:
#     print(user["name"])
# else:
#     print("Usuario no encontrado")
