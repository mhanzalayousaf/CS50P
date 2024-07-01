import csv
import sys


def main():
    check_command_line_arg()
    new_students_format = list()

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(",")
                house = row["house"]
                new_students_format.append(
                    {
                        "first": first.lstrip(),
                        "last": last,
                        "house": house
                    }
                )

        with open(sys.argv[2], "w", newline='') as file:
            writer = csv.DictWriter(
                file, fieldnames=["first", "last", "house"]
            )
            writer.writeheader()
            writer.writerows(new_students_format)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


def check_command_line_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv") or not sys.argv[1].endswith(".csv"):
        sys.exit("File is not CSV")


if __name__ == "__main__":
    main()
