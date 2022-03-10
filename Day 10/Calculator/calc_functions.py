from art import logo
# add


def add(n1, n2):
    """Adds two numbers."""
    return n1 + n2

# subtract


def subtract(n1, n2):
    """Subtracts two numbers."""
    return n1 - n2

# Multiply


def multiply(n1, n2):
    """Multiply two numbers."""
    return n1 * n2

# divide


def divide(n1, n2):
    """Divides two numbers."""
    return n1 / n2


operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide,
              }


def calculator():
    print(logo)
    first_number = float(input("What is the first number?: "))

    second_number = float(input("What is the second number?: "))

    for symbol in operations:
        print(symbol)

    operation_symbol = input("Pick an operation: ")

    calculation_function = operations[operation_symbol]
    answer = calculation_function(first_number, second_number)

    print(f"{first_number} {operation_symbol} {second_number} = {answer}")

    to_continue = input(
        f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ").lower()

    while(to_continue == 'y'):

        first_number = answer

        operation_symbol = input("Pick an operation: ")

        second_number = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]

        answer = calculation_function(first_number, second_number)

        print(f"{first_number} {operation_symbol} {second_number} = {answer}")

        to_continue = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ").lower()


calculator()
