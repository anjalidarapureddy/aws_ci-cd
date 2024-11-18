def calculator():
    import sys

    # Use command-line arguments for input
    args = sys.argv[1:]

    if len(args) != 3:
        print("Usage: python app.py <operation> <num1> <num2>")
        print("Example: python app.py add 10 20")
        return

    operation, num1, num2 = args
    num1, num2 = float(num1), float(num2)

    if operation == "add":
        print(f"Result: {add(num1, num2)}")
    elif operation == "subtract":
        print(f"Result: {subtract(num1, num2)}")
    elif operation == "multiply":
        print(f"Result: {multiply(num1, num2)}")
    elif operation == "divide":
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid operation. Use 'add', 'subtract', 'multiply', or 'divide'.")
