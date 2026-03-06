def main():
    answer = input("What time is it? ")
    time = convert(answer)
 
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")
 
 
def convert(time):
    if "a.m." in time or "p.m." in time:
        time_part, suffix = time.split(" ")
        hours, minutes = time_part.split(":")
        hours = float(hours)
        minutes = float(minutes)
 
        if suffix == "p.m." and hours != 12:
            hours += 12
        elif suffix == "a.m." and hours == 12:
            hours = 0
    else:
        hours, minutes = time.split(":")
        hours = float(hours)
        minutes = float(minutes)
 
    return hours + (minutes / 60)
 
 
if __name__ == "__main__":
    main()