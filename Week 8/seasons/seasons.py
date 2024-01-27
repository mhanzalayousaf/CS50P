from datetime import date
import inflect
import sys
import re


p = inflect.engine()


def main():
    birth_date = input("Date of Birth: ")
    try:
        year, month, day = check_birthdate(birth_date)
    except ValueError:
        sys.exit("Invalid date")
    date_of_birth = date(int(year), int(month), int(day))
    date_of_today = date.today()
    diff = date_of_today - date_of_birth
    total_minutes = diff.days * 365 * 24 * 60
    output = p.number_to_words(total_minutes, andword="").capitalize()
    print(f"{output} minutes")


def check_birthdate(birth_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
        year, month, day = birth_date.split("-")
        return (year, month, day)


if __name__ == "__main__":
    main()