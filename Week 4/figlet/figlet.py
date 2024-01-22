import sys
from pyfiglet import Figlet


if len(sys.argv) == 1:
    figlet = Figlet()
    user_input = input("Input: ")
    print(figlet.renderText(user_input))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    font_name = sys.argv[2]
    figlet = Figlet(font=font_name)
    user_input = input("Input: ")
    print(figlet.renderText(user_input))
else:
    print("Invalid usage")
    sys.exit(1)
