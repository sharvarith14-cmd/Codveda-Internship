============================================
# Codveda Internship - Level 1, Task 1
# Simple Calculator
# Author: Sharvari Yogeshsingh Thakur
# ============================================

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """Returns the division of a by b. Handles division by zero."""
    if b == 0:
        return "Error: Division by zero is not allowed!"
    return a / b

def calculator():
    print("=" * 40)
    print("       Welcome to Simple Calculator")
    print("=" * 40)

    while True:
        print("\nSelect an operation:")
        print("  1. Addition       (+)")
        print("  2. Subtraction    (-)")
        print("  3. Multiplication (*)")
        print("  4. Division       (/)")
        print("  5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == '5':
            print("\nThank you for using the calculator. Goodbye!")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Invalid choice! Please enter a number between 1 and 5.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if choice == '1':
            result = add(num1, num2)
            operator = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operator = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operator = '*'
        elif choice == '4':
            result = divide(num1, num2)
            operator = '/'

        if isinstance(result, str):
            print(f"\n{result}")
        else:
            # Display as int if result is a whole number
            display = int(result) if result == int(result) else result
            print(f"\nResult: {num1} {operator} {num2} = {display}")

if __name__ == "__main__":
    calculator()