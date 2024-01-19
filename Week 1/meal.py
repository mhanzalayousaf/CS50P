def main():
    timeinput = input("What time it is? ")
    mealtime = convert(timeinput)
    if 7.0 <= mealtime <= 8.0:
        print("breakfast time")
    elif 12.0 <= mealtime <= 13.0:
        print("lunch time")
    elif 18.0 <= mealtime <= 19.0:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hoursinput = int(hours)
    minutesinput = int(minutes)
    totaltime = hoursinput + minutesinput/60
    return totaltime


if __name__ == "__main__":
    main()