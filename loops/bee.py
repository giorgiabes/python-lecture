WORDS = {
    "PAIR": 4,
    "HEAR": 4,
    "CHEAR": 5,
    "GRAPHIC": 7,
}


def main():
    count = 0
    print("Welcome to Spelling Bee!")
    print("Here is yesterday's answers:")

    for word, points in WORDS.items():
        print(f"{word} was worth {points} points.")


main()
