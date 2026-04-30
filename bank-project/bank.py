import json
import os
from getpass import getpass

DB_FILE = "db.json"


def load_db():
    if not os.path.exists(DB_FILE):
        return {"users": {}}
    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_db(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=2)


def register():
    username = input("Choose a username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return
    db = load_db()
    if username in db["users"]:
        print("That username is already taken.")
        return
    password = getpass("Choose a password: ")
    if not password:
        print("Password cannot be empty.")
        return
    db["users"][username] = {
        "password": password,
        "balance": 0.0,
        "transactions": [],
    }
    save_db(db)
    print(f"Account created for '{username}'")


def login():
    username = input("Username: ").strip()
    password = getpass("Password: ")
    db = load_db()
    user = db["users"].get(username)
    if user is None or user["password"] != password:
        print("Invalid username or password")
        return None
    print(f"Welcome back, {username}")
    return username


def main():
    while True:
        print("\n=== Simple Bank ===")
        print("1. Register")
        print("2. Login")
        print("3. Quit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                print(f"(Banking menu for '{user}' comming in the next lecture)")
        elif choice == "3":
            print("Goodbye!")
            return
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
