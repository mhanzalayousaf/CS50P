import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if iscorrectformat := re.search(
        r"^(([0-9][0-2]*):*([0-5][0-9])*) (AM|PM) to (([0-9][0-2]*):*([0-5][0-9])*) (AM|PM)$",
        s,
    ):
        pieces = iscorrectformat.groups()
        if int(pieces[1]) > 12 and int(pieces[5]) > 12:
            raise ValueError
        first_time = new_format(pieces[1], pieces[2], pieces[3])
        second_time = new_format(pieces[5], pieces[6], pieces[7])
        return f"{first_time} to {second_time}"
    else:
        raise ValueError


def new_format(hour, minute, am_pm):
    if am_pm == "PM":
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)

    if minute == None:
        new_minute = ":00"
        new_time = f"{new_hour:02}" + new_minute
    else:
        new_time = f"{new_hour:02}" + ":" + minute

    return new_time


if __name__ == "__main__":
    main()