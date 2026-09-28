accounts = {1: 1000, 2: 500}


def transfer_money(from_account, to_account, amount):
    if amount <= 0:
        raise ValueError("Monto inválido")

    if accounts[from_account] < amount:
        raise ValueError("Saldo insuficiente")

    accounts[from_account] -= amount
    accounts[to_account] += amount

    return {"status": "success", "amount": amount}


transfer_money(1, 2, 200)
print(accounts)
