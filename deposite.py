from utilis import add_transaction


def deposit(account, amount):
    if amount <= 0:
        return "Invalid amount."

    account["balance"] = round(account["balance"] + amount, 2)
    add_transaction(account, "Deposit", amount)
    return "Deposit successful."
