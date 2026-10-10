class BankAccount:
    def __init__(self, account_id, balance=0):
        self.id = account_id
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Monto inválido")

        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Monto inválido")

        if amount > self._balance:
            raise ValueError("Saldo insuficiente")

        self._balance -= amount


account = BankAccount(account_id=101, balance=1000)

account.deposit(500)
account.withdraw(200)

print(account.balance)
