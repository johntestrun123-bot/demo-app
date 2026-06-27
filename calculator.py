def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    operations = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
    }

    print("Simple Calculator")
    print("-----------------")

    while True:
        print("\nOperations:")
        print("  1. Add")
        print("  2. Subtract")
        print("  3. Multiply")
        print("  4. Divide")
        print("  q. Quit")

        choice = input("\nSelect operation: ").strip().lower()

        if choice == "q":
            print("Goodbye!")
            break

        if choice not in operations:
            print("Invalid choice. Please select 1-4 or q.")
            continue

        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        symbol, func = operations[choice]
        try:
            result = func(a, b)
            print(f"Result: {a} {symbol} {b} = {result}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
