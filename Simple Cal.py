def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract two numbers."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide two numbers."""
    if y == 0:
        return "Error! Division by zero."
    return x / y

def get_number(prompt):
    """Get a valid number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_operation():
    """Get a valid operation from the user."""
    operations = {'1': 'Add', '2': 'Subtract', '3': 'Multiply', '4': 'Divide'}
    for key, value in operations.items():
        print(f"{key}. {value}")
    while True:
        choice = input("Choose an operation (1/2/3/4): ")
        if choice in operations:
            return choice
        print("Invalid choice. Please choose a valid operation.")

def main():
    """Main function to run the calculator."""
    print("Simple Calculator")
    
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    
    operation = get_operation()
    
    if operation == '1':
        result = add(num1, num2)
    elif operation == '2':
        result = subtract(num1, num2)
    elif operation == '3':
        result = multiply(num1, num2)
    elif operation == '4':
        result = divide(num1, num2)
    
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
