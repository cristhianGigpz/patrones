class Exporter:
    def __init__(self):
        self.plugins = {}

    def register(self, name, plugin):
        self.plugins[name] = plugin

    def export(self, name, data):
        plugin = self.plugins[name]
        return plugin.export(data)


class JSONPlugin:
    def export(self, data):
        import json

        return json.dumps(data)


class CSVPlugin:
    def export(self, data):
        return ",".join(data.keys()) + "\n" + ",".join(map(str, data.values()))


exporter = Exporter()

exporter.register("json", JSONPlugin())
exporter.register("csv", CSVPlugin())

data = {"name": "Cristian", "age": 25}

print(exporter.export("json", data))
print(exporter.export("csv", data))
