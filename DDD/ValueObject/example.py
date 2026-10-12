from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Money:
    amount: Decimal
    currency: str

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Importe inválido")

        if not self.currency:
            raise ValueError("Moneda obligatoria")

    def add(self, other: "Money") -> "Money":

        if self.currency != other.currency:
            raise ValueError("No se pueden sumar monedas diferentes")

        return Money(self.amount + other.amount, self.currency)


class Product:
    def __init__(self, product_id: int, name: str, price: Money):
        self.id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"Producto(id={self.id}, nombre={self.name}, precio={self.price.amount} {self.price.currency})"

    def change_price(self, new_price: Money):
        self.price = new_price


price1 = Money(Decimal("150.00"), "PEN")

price2 = Money(Decimal("150.00"), "PEN")

print(price1 == price2)
print(price1 is price2)

price = Money(Decimal("150.00"), "PEN")

##price.amount = Decimal("200.00")
##new_price = Money(Decimal("200.00"), "PEN")

price1 = Money(Decimal("100.00"), "PEN")

price2 = Money(Decimal("50.00"), "PEN")

total = price1.add(price2)

print(total)

# price1 = Money(Decimal("100.00"), "PEN")

# price2 = Money(Decimal("50.00"), "USD")

# total = price1.add(price2)

product = Product(product_id=1, name="Laptop", price=Money(Decimal("2500.00"), "PEN"))
product.change_price(Money(Decimal("2300.00"), "PEN"))
print(product.price)
print(product)
