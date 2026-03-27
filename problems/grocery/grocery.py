def main():
    grocery = {}
    get_items(grocery)
    print_items(grocery)


def get_items(items):
    while True:
        try:
            user_input = input("")
            if user_input in items:
                items[user_input] += 1
            else:
                items[user_input] = 1
        except EOFError:
            break


def print_items(items):
    for k in sorted(items):
        print(items[k], k.upper())


main()
