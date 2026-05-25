from datetime import datetime
import os
import json
from getpass import getpass


"""
Transaction object -> to_dict() -> plain dict -> json.dump -> text on disk
                                                                    |
                                                                    |
Transaction object <- from_dict() <- plain dict <- json.load <- text on dist
"""


class Transactions:
    def __init__(self, type, amount, to=None, from_=None, at=None):
        self.type = type
        self.amount = amount
        self.to = to
        self.from_ = from_
        self.at = at or datetime.now().isoformat(timespec="seconds")

    def to_dict(self):
        data = {"type": self.type, "amount": self.amount, "at": self.at}
        if self.to is not None:
            data["to"] = self.to
        if self.from_ is not None:
            data["from"] = self.from_
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(
            type=data["type"],
            amount=data["amount"],
            to=data.get("to"),
            from_=data.get("from"),
            at=data.get("at"),
        )


class Account:
    def __init__(self, username, password, balance=0.0, transactions=None):
        self.username = username
        self.password = password
        self.balance = balance
        self.transactions = transactions if transactions is not None else []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transactions("deposit", amount))

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self.transactions.append(Transactions("withdraw", amount))

    def record_transfer_out(self, amount, to):
        self.balance -= amount
        self.transactions.append(Transactions("transfer_out", amount, to=to))

    def record_transfer_in(self, amount, from_):
        self.balance += amount
        self.transactions.append(
            Transactions(
                "transfer_in",
                amount,
                from_=from_,
            )
        )

    def to_dict(self):
        return {
            "password": self.password,
            "balance": self.balance,
            "transactions": [t.to_dict() for t in self.transactions],
        }

    @classmethod
    def from_dict(cls, username, data):
        return cls(
            username=username,
            password=data["password"],
            balance=data["balance"],
            transactions=[
                Transactions.from_dict(t) for t in data.get("transactions", [])
            ],
        )


class Bank:
    DB_FILE = "db.json"

    def __init__(self, db_file=None):
        self.db_file = db_file or self.DB_FILE
        self.accounts = {}
        self.load()

    def load(self):
        if not os.path.exists(self.db_file):
            self.accounts = {}
            return

        with open(self.db_file, "r") as f:
            data = json.load(f)

        self.accounts = {
            username: Account.from_dict(username, user_data)
            for username, user_data in data.get("users", {}).items()
        }

    def save(self):
        data = {"users": {a.username: a.to_dict() for a in self.accounts.values()}}

        with open(self.db_file, "w") as f:
            json.dump(data, f, indent=2)

    def register(self, username, password):
        if username in self.accounts:
            raise ValueError("That username is already taken.")

        account = Account(username, password)
        self.accounts[username] = account
        self.save()
        return account

    def authenticate(self, username, password):
        account = self.accounts.get(username)
        if account is None or account.password != password:
            return None
        return account


class BankApp:
    def __init__(self):
        self.bank = Bank()
        self.current_user = None

    def run(self):
        while True:
            print("\n=== Mega Bank ===")
            print("1. Register")
            print("2. Quit")
            choice = input("Choose an option: ").strip()
            if choice == "1":
                self._register()
            elif choice == "2":
                print("Goodbye!")
                return
            else:
                print("Ivalid choice.")

    def _register(self):
        username = input("Choose a username: ").strip()
        if not username:
            print("Username cannot be empty.")
            return
        password = getpass("Choose a password: ")

        if not password:
            print("Password cannot be empty.")
            return

        try:
            self.bank.register(username, password)
        except ValueError as e:
            print(e)
            return
        print(f"Account created for '{username}.'")

    def _login(self):
        username = input("Username: ").strip()
        password = getpass("Password: ").strip()
        account = self.bank.authenticate(username, password)
        if account is None:
            print("Ivalid username or password")
            return
        self.current_user = account
        print(f"Welcome back, {account.username}")
        print("(Bank menu comming in the next lecture)")


if __name__ == "__main__":
    BankApp().run()
