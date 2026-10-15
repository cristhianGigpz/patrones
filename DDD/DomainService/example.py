from decimal import Decimal


class BankAccount:
    def __init__(self, account_id, balance):
        self.id = account_id
        self._balance = Decimal(balance)

    @property
    def balance(self):
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Monto inválido")

        if amount > self._balance:
            raise ValueError("Saldo insuficiente")

        self._balance -= amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Monto inválido")

        self._balance += amount


class TransferService:
    def transfer(self, source, destination, amount):

        if source.id == destination.id:
            raise ValueError("No se puede transferir a la misma cuenta")

        if amount <= 0:
            raise ValueError("Monto inválido")

        source.withdraw(amount)
        destination.deposit(amount)


account1 = BankAccount(1, "1000")
account2 = BankAccount(2, "500")

service = TransferService()

service.transfer(account1, account2, Decimal("200.00"))

print(account1.balance)
print(account2.balance)
