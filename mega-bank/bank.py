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
        if amount < 0:
            return
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

    def transfer(self, sender, recipient_username, amount):
        if recipient_username == sender.username:
            raise ValueError("You cannot transfer to yourself.")
        recipient = self.accounts.get(recipient_username)
        if recipient is None:
            raise ValueError("That user doesnot exist.")
        if amount > sender.balance:
            raise ValueError("Insufficient funds.")
        sender.record_transfer_out(amount, to=recipient_username)
        recipient.record_transfer_in(amount, from_=sender.username)
        self.save()


class BankApp:
    def __init__(self):
        self.bank = Bank()
        self.current_user = None

    def run(self):
        while True:
            print("\n=== Mega Bank ===")
            print("1. Register")
            print("2. Login")
            print("3. Quit")
            choice = input("Choose an option: ").strip()
            if choice == "1":
                self._register()
            elif choice == "2":
                self._login()
            elif choice == "3":
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
        self._user_menu()

    def _user_menu(self):
        while True:
            user = self.current_user
            if user is None:
                return
            print(f"\n--- Logged in as {user.username} ---")
            print("1. Check balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Transaction history")
            print("6. Logout")
            choice = input("Choose an option: ").strip()
            if choice == "1":
                self._show_balance()
            elif choice == "2":
                self._deposit()
            elif choice == "3":
                self._withdraw()
            elif choice == "4":
                self._transfer()
            elif choice == "5":
                self._show_history()
            elif choice == "6":
                print("Logged out.")
                self.current_user = None
                return
            else:
                print("Invalid choice.")

    def _show_balance(self):
        user = self.current_user
        if user is None:
            return
        print(f"Current balance: ${user.balance:.2f}")

    def _read_amount(self, prompt):
        raw = input(prompt).strip()
        try:
            amount = float(raw)
        except ValueError:
            print("That's not valid number.")
            return None
        return round(amount, 2)

    def _deposit(self):
        amount = self._read_amount("Amount to deposit: $")
        user = self.current_user
        if amount is None:
            return
        if amount < 0:
            print("deposit cannot be negativ number")
            return
        if user is None:
            return

        user.deposit(amount)
        self.bank.save()
        print(f"Deposited ${amount:.2f}. New balance: ${user.balance:.2f}")

    def _withdraw(self):
        user = self.current_user
        if user is None:
            return
        amount = self._read_amount("Amount to withdraw: $")
        if amount is None:
            return
        try:
            user.withdraw(amount)
        except ValueError as e:
            print(e)
            return
        self.bank.save()
        print(f"Withdrew ${amount:.2f}. New balance: ${user.balance:.2f}")

    def _transfer(self):
        user = self.current_user
        if user is None:
            return
        recipient = input("Recipient username: ").strip()
        amount = self._read_amount("Amount to transfer: $")
        if amount is None:
            return
        try:
            self.bank.transfer(self.current_user, recipient, amount)
        except ValueError as e:
            print(e)
            return
        print(
            f"Transferred ${amount:.2f} to {recipient}. New balance: ${user.balance:.2f}"
        )

    def _show_history(self):
        user = self.current_user
        if user is None:
            return
        txs = user.transactions
        if not txs:
            print("No transactions yet.")
            return
        print("\n--- Transaction History ---")
        for t in txs:
            line = f"[{t.at}] {t.type:<13} ${t.amount:.2f}"
            if t.to is not None:
                line += f" -> {t.to}"
            if t.from_ is not None:
                line += f" <- {t.from_}"
            print(line)


if __name__ == "__main__":
    BankApp().run()
