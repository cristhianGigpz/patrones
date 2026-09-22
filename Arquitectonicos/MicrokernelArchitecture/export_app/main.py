from core.exporter import Exporter

from plugins.json_plugin import JSONPlugin
from plugins.csv_plugin import CSVPlugin


app = Exporter()

app.register("json", JSONPlugin())
app.register("csv", CSVPlugin())

data = {"name": "Cristian", "role": "Developer"}

print(app.export("json", data))
print(app.export("csv", data))
