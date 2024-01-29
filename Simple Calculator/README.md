# Simple Calculator

## Video Demo:
\[https://youtu.be/laf3XPAjtK0\]

## Description:
The Simple Calculator project is a basic calculator implemented in Python. It provides users with the ability to perform standard arithmetic operations (addition, subtraction, multiplication, and division) along with additional functions for calculating the square, square root, and factorial of both numbers entered by the user.

## Project Structure:

### project.py
- **main():** Entry point of the program. Accepts user input for two numbers and the desired operation.
- **perform_arithmetic_operation(choice, num1, num2):** Performs standard arithmetic operations based on user choice.
- **square(num1, num2):** Calculates the square of both numbers.
- **square_root(num1, num2):** Calculates the square root of both numbers.
- **factorial(num1, num2):** Calculates the factorial of both numbers.

### test_project.py
- **test_addition():** Tests the addition function.
- **test_subtraction():** Tests the subtraction function.
- **test_multiplication():** Tests the multiplication function.
- **test_division():** Tests the division function.
- **test_square():** Tests the square function.
- **test_square_root():** Tests the square root function.
- **test_factorial():** Tests the factorial function.
- **test_invalid_factorial():** Tests the factorial function with invalid input.

## How to Run:
1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the main program using `python project.py`.
4. Run tests using `pytest` to ensure the correctness of the implemented functions.