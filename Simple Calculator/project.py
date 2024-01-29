# project.py

def main():
    print("Simple Calculator")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square (of both numbers)")
    print("6. Square Root (of both numbers)")
    print("7. Factorial (of both numbers)")

    choice = input("Enter choice (1-7): ")

    if choice in ["1", "2", "3", "4"]:
        result = perform_arithmetic_operation(choice, num1, num2)
        print(f"Result: {result}")
    elif choice == "5":
        result1, result2 = square(num1, num2)
        print(f"Square of {num1}: {result1}")
        print(f"Square of {num2}: {result2}")
    elif choice == "6":
        result1, result2 = square_root(num1, num2)
        print(f"Square Root of {num1}: {result1}")
        print(f"Square Root of {num2}: {result2}")
    elif choice == "7":
        result1, result2 = factorial(num1, num2)
        print(f"Factorial of {num1}: {result1}")
        print(f"Factorial of {num2}: {result2}")
    else:
        print("Invalid choice")


def perform_arithmetic_operation(choice, num1, num2):
    if choice == "1":
        return num1 + num2
    elif choice == "2":
        return num1 - num2
    elif choice == "3":
        return num1 * num2
    elif choice == "4":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"


def square(num1, num2):
    return num1**2, num2**2


def square_root(num1, num2):
    return num1**0.5, num2**0.5


def factorial(num1, num2):
    def calculate_factorial(num):
        if num == int(num) and num >= 0:
            if num == 0:
                return 1
            else:
                return num * calculate_factorial(num - 1)
        else:
            return "Factorial is only defined for non-negative integers."

    return calculate_factorial(num1), calculate_factorial(num2)


if __name__ == "__main__":
    main()
