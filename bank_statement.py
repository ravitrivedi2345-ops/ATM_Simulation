def show_statement(account):
    print("\n--- TRANSACTION STATEMENT ---")
    print(f"Current Balance: Rs. {account['balance']:.2f}")

    transactions = account.get("transactions", [])
    if not transactions:
        print("No transactions found.")
        return

    print("\nRecent Transactions:")
    for tx in transactions:
        print(
            f"{tx['time']} | {tx['type']} | "
            f"Amount: Rs. {tx['amount']:.2f} | "
            f"Balance: Rs. {tx['balance_after']:.2f}"
        )
