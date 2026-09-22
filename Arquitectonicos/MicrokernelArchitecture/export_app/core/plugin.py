from typing import Protocol


class ExportPlugin(Protocol):
    def export(self, data: dict) -> str: ...
