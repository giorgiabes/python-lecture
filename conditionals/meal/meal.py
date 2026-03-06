def main():
    time = input("What time is it? ")
    if 7 <= convert(time) <= 8:
        print("breakfast time")
    elif 12 <= convert(time) <= 13:
        print("lunch time")
    elif 18 <= convert(time) <= 19:
        print("dinner time")


def convert(time):
    if "a.m." in time or "p.m." in time:
        t, y = time.split(" ")
        h, m = t.split(":")
        if y == "p.m.":
            result = 12 + int(h) + int(m) / 60
        else:
            result = int(h) + int(m) / 60
        return result
    else:
        h, m = time.split(":")
        result = int(h) + int(m) / 60
        return result

if __name__ == "__main__":
    main()
