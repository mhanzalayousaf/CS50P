from PIL import Image, ImageOps
import sys


def main():
    check_command_line_arg()

    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exists.")

    shirtfile = Image.open("shirt.png")
    size = shirtfile.size
    muppet = ImageOps.fit(imagefile, size)
    muppet.paste(shirtfile, shirtfile)
    muppet.save(sys.argv[2])


def check_command_line_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    types = (".jpg", ".jpeg", ".png")
    if not sys.argv[1].endswith(types) or not sys.argv[2].endswith(types):
        sys.exit("Input an Output have different extensions")


if __name__ == "__main__":
    main()
