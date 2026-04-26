import json
from datetime import datetime
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "account_data.json")


def default_account():
    return {
        "account_number": "1234567890",
        "pin": "1234",
        "holder_name": "Student User",
        "balance": 1000.0,
        "transactions": [],
    }


def load_account():
    if not os.path.exists(DATA_FILE):
        account = default_account()
        save_account(account)
        return account

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as fp:
            data = json.load(fp)
    except Exception:
        account = default_account()
        save_account(account)
        return account

    account = default_account()
    if isinstance(data, dict):
        account.update(data)
    try:
        account["balance"] = float(account["balance"])
    except Exception:
        account["balance"] = 0.0
    if type(account.get("transactions")) is not list:
        account["transactions"] = []
    return account


def save_account(account):
    with open(DATA_FILE, "w", encoding="utf-8") as fp:
        json.dump(account, fp, indent=2)


def prompt_amount(message):
    while True:
        raw = input(message).strip()
        try:
            amount = float(raw)
        except Exception:
            print("Enter valid number.")
            continue

        if amount <= 0:
            print("Amount should be greater than 0.")
            continue

        return round(amount, 2)


def add_transaction(account, tx_type, amount):
    record = {
        "type": tx_type,
        "amount": round(amount, 2),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "balance_after": round(account["balance"], 2),
    }
    account["transactions"].append(record)
