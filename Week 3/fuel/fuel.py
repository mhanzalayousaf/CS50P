while True:
    fuel = input("Fraction: ")

    try:
        numerator, denominator = fuel.split("/")
        x = int(numerator)
        y = int(denominator)
        f = x / y
        if f <= 1:
            break
    
    except (ValueError, ZeroDivisionError):
        pass

percentage = int(f * 100)
if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")