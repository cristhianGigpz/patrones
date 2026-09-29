# def withdraw(account, amount):

#     if amount <= 0:
#         raise ValueError("Monto inválido")

#     if account["balance"] < amount:
#         raise ValueError("Saldo insuficiente")

#     account["balance"] -= amount


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Monto inválido")

        if self.balance < amount:
            raise ValueError("Saldo insuficiente")

        self.balance -= amount


account = BankAccount(1000)

account.withdraw(200)

print(account.balance)
