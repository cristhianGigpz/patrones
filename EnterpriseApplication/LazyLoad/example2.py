from functools import cached_property


class Report:
    def __init__(self, sales):
        self.sales = sales

    @cached_property
    def total(self):

        print("Calculando total...")

        return sum(self.sales)


report = Report([100, 200, 300, 400])

print("Reporte creado")
print(report.total)
print(report.total)
