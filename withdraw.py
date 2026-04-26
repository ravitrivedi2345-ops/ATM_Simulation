from utilis import add_transaction


def withdraw(account, amount):
    if amount <= 0:
        return "Invalid amount."

    if amount > account["balance"]:
        return "Insufficient balance."

    account["balance"] = round(account["balance"] - amount, 2)
    add_transaction(account, "Withdraw", amount)
    return "Withdrawal successful."
