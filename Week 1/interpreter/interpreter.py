expression = input("Expression: ")

x, y, z = expression.split()

x = int(x)
z = int(z)

if y == "+":
    print(f"{x + z:.1f}")
elif y == "-":
    print(f"{x - z:.1f}")
elif y == "*":
    print(f"{x * z:.1f}")
elif y == "/":
    if z == 0:
        print("Division by zero is not allowed.")
    else:
        print(f"{x / z:.1f}")
else:
    print("Invalid operator. Please use +, -, *, or /")
