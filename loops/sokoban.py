def main():
    history = []

    while True:
        action = input("Action: ")

        if action == "Undo":
            undone = history.pop()
            print(f"Undone: '{undone}'")
        elif action == "Restart":
            history.clear()
        else:
            history.append(action)

        print(history)


# def calculate_index(lst):
#     sum = 0
#     for i in range(len(lst)):
#         sum += i

#     return round(sum / len(lst))


main()
