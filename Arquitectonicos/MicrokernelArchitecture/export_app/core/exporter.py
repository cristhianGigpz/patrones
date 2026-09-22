from .plugin import ExportPlugin


class Exporter:
    def __init__(self):
        self.plugins: dict[str, ExportPlugin] = {}

    def register(self, name: str, plugin: ExportPlugin):
        self.plugins[name] = plugin

    def export(self, name: str, data: dict) -> str:
        plugin = self.plugins[name]

        return plugin.export(data)
