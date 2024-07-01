import sys

from PIL import Image, ImageOps


def main():
    check_command_line_arg()

    try:
        image = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        new_image = ImageOps.fit(image, shirt.size)
        new_image.paste(shirt, mask=shirt)
        new_image.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit(f"Could not find {sys.argv[1]}")


def check_command_line_arg():
    extensions = ['jpg', 'jpeg', 'png']

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    try:
        root_1, extension_1 = sys.argv[1].split(".")
        root_2, extension_2 = sys.argv[2].split(".")

        if extension_1 != extension_2:
            sys.exit("Input and output have different extentions")
        if not extension_1 in extensions and not extension_2 in extensions:
            sys.exit("Invalid input")
    except ValueError:
        sys.exit("Invalid input")


if __name__ == "__main__":
    main()

    types = (".jpg", ".jpeg", ".png")
    if not sys.argv[1].endswith(types) or not sys.argv[2].endswith(types):
        sys.exit("Input an Output have different extensions")


if __name__ == "__main__":
    main()
