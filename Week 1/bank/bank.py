users_input = input("Greeting: ").lower().lstrip()

if users_input.startswith("Hello"):
    print("$0")
elif users_input.startswith("h"):
    print("$20")
else:
    print("$100")