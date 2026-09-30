"""
accounts
┌────┬─────────┐
│ id │ balance │
├────┼─────────┤
│ 1  │ 1000    │
│ 2  │ 500     │
└────┴─────────┘
"""


class AccountTable:
    def __init__(self):
        self.accounts = {1: {"balance": 1000}, 2: {"balance": 500}}

    def transfer(self, source_id, target_id, amount):
        source = self.accounts[source_id]
        target = self.accounts[target_id]

        if amount <= 0:
            raise ValueError("Monto inválido")

        if source["balance"] < amount:
            raise ValueError("Saldo insuficiente")

        source["balance"] -= amount
        target["balance"] += amount


accounts = AccountTable()

accounts.transfer(source_id=1, target_id=2, amount=200)

print(accounts.accounts)
