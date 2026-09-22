import json


class JSONPlugin:
    def export(self, data: dict) -> str:
        return json.dumps(data)
