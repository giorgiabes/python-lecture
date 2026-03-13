def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for name in names:
        print(write_letter(name, "Princess Peach"))

# range(4) => [0, 1, 2, 3]

def write_letter(receiver, sender):
    return f"""
    +--------------------------------------------------+
    Dear {receiver}

    You are cordially invited to a ball at
    Peach's Clastle this evning, 7:00 PM.

    Sincerely,
    {sender}
    +--------------------------------------------------+
    """

main()