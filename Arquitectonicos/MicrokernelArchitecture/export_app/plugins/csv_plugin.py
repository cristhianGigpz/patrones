import csv
from io import StringIO


class CSVPlugin:
    def export(self, data: dict) -> str:
        output = StringIO()

        writer = csv.DictWriter(output, fieldnames=data.keys())

        writer.writeheader()
        writer.writerow(data)

        return output.getvalue().strip()
