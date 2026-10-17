from decimal import Decimal
from uuid import uuid4


class BankAccount:
    def __init__(self, account_id, account_type, balance, withdrawal_limit):
        self.id = account_id
        self.type = account_type
        self.balance = balance
        self.withdrawal_limit = withdrawal_limit


class BankAccountFactory:
    @staticmethod
    def create(account_type, initial_balance):

        balance = Decimal(str(initial_balance))

        if balance < 0:
            raise ValueError("Saldo inválido")

        if account_type == "savings":
            withdrawal_limit = Decimal("1000.00")

        elif account_type == "checking":
            withdrawal_limit = Decimal("5000.00")

        else:
            raise ValueError("Tipo de cuenta no permitido")

        return BankAccount(
            account_id=str(uuid4()),
            account_type=account_type,
            balance=balance,
            withdrawal_limit=withdrawal_limit,
        )


account1 = BankAccountFactory.create("savings", 500)

account2 = BankAccountFactory.create("checking", 2000)

print(account1.withdrawal_limit)
print(account2.withdrawal_limit)
