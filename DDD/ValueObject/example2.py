from dataclasses import dataclass


@dataclass(frozen=True)
class Address:
    street: str
    city: str
    country: str


address1 = Address("Av. Principal 123", "Lima", "Perú")

address2 = Address("Av. Principal 123", "Lima", "Perú")

print(address1 == address2)

customer_name = "Carlos"
customer_email = "carlos@gmail.com"
customer_age = 25


@dataclass(frozen=True)
class Email:
    value: str

    def __post_init__(self):
        if "@" not in self.value:
            raise ValueError("Email inválido")


email = Email("carlos@gmail.com")
print(email)
