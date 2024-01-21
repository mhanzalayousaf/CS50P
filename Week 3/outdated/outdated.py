months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


while True:
    date_input = input("Date: ")

    try:
        month, day, year = date_input.split("/")
        if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
            break

    except:
        try:
            old_month, old_day, year = date_input.split(" ")
            for i in range(len(months)):
                if old_month == months[i]:
                    month = i + 1
                    break
                if not old_day.endswith(","):
                    continue
            day = old_day.replace(",", "")
            if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
                break

        except:
            pass


print(f"{year}-{int(month):02}-{int(day):02}")
