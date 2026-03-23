def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str) -> bool:
    if s.isalpha():
        if first_two_alpha(s) and min_max(s):
            return True
    else:
        if first_two_alpha(s) and min_max(s) and middle_number(s) and first_not_zero(s):
            return True


def first_two_alpha(s: str) -> bool:
    return s[:2].isalpha()


def min_max(s: str) -> bool:
    return 2 <= len(s) <= 6


def middle_number(s: str) -> bool:
    # If a number appears in the sting, it must be
    # followed by numbers until the end
    return s[get_index(s) :].isdigit()


def first_not_zero(s: str):
    # Check if first number is not zero
    return s[get_index(s) :][0] != "0"


def get_index(s: str) -> int:
    # Get the index of the first occurrence of a
    # number in the string.
    for i in range(len(s)):
        if s[i].isdigit():
            return i


main()
