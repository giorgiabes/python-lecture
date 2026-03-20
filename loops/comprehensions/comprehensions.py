from helpers import get_words, save_counts


def main():
    counts = {}
    words = get_words("address.txt")
    lst = [word.lower() for word in words]

    for word in lst:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    save_counts(counts)


main()
