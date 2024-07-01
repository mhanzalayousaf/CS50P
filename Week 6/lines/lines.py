import sys

lines_count = 0

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few commad-line arguements")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a python file")
else:
    try:
        with open(sys.argv[1], "r") as file:
            for line in file:
                if line.strip() and not line.lstrip().startswith("#"):
                    lines_count += 1

        print(lines_count)

    except FileNotFoundError:
        sys.exit("File does not exist")
