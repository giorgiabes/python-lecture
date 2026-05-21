from datetime import datetime


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


if __name__ == "__main__":
    alice = Account("alice", "testpass123")
    alice.deposit(100.0)
    alice.withdraw(30.0)
    print(alice.to_dict())
