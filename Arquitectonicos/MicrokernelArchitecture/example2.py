class Application:
    def __init__(self):
        self.commands = {}

    def register(self, name, command):
        self.commands[name] = command

    def execute(self, name):
        self.commands[name].run()


class HelloPlugin:
    def run(self):
        print("¡Hola mundo!")


class GoodbyePlugin:
    def run(self):
        print("¡Hasta luego!")


app = Application()

app.register("hello", HelloPlugin())
app.register("goodbye", GoodbyePlugin())

app.execute("hello")
app.execute("goodbye")

"""
def export(format, data):

    if format == "json":
        # Exportar JSON
        ...

    elif format == "csv":
        # Exportar CSV
        ...

    elif format == "xml":
        # Exportar XML
        ...
"""
