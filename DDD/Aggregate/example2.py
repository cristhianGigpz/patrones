class BankAccount:
    def __init__(self, account_id, balance=0):
        if balance < 0:
            raise ValueError("Saldo inválido")

        self.id = account_id
        self._balance = balance
        self._transactions = []

    @property
    def balance(self):
        return self._balance

    @property
    def transactions(self):
        return tuple(self._transactions)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Monto inválido")

        self._balance += amount
        self._transactions.append(("deposit", amount))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Monto inválido")

        if amount > self._balance:
            raise ValueError("Saldo insuficiente")

        self._balance -= amount
        self._transactions.append(("withdrawal", amount))


account = BankAccount(101, 1000)

account.deposit(500)
account.withdraw(200)

print(account.balance)
print(account.transactions)

"""
with unit_of_work as uow:

    order = uow.orders.find_by_id(101)

    order.add_item(
        product_id=3,
        quantity=2,
        price=Decimal("50")
    )

    uow.orders.save(order)
"""
