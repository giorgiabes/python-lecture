def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Odd")
    else:
        print("Even")

def is_even(n):
    return n % 2 == 0 
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False

main()