# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def add_values(first_num, second_num):
    return first_num + second_num


def subtract_values(first_num, second_num):
    return first_num - second_num


def multiply_values(first_num, second_num):
    return first_num * second_num


def divide_values(first_num, second_num):
    if second_num == 0:
        return None
    return round(first_num / second_num, 2)


def modulus_values(first_num, second_num):
    if second_num == 0:
        return None
    return first_num % second_num


def power_values(first_num, second_num):
    return first_num ** second_num


def print_calculator_menu():
    print("\n============================")
    print("        SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def format_number(val):
    if val.is_integer():
        return int(val)
    return val


def main():
    while True:
        print_calculator_menu()
        user_choice = input("Select an operation (1-7): ").strip()

        if user_choice == "7":
            print("Goodbye!")
            break

        if user_choice in ["1", "2", "3", "4", "5", "6"]:
            try:
                first_input = float(input("Enter first number : "))
                second_input = float(input("Enter second number: "))

                num1 = format_number(first_input)
                num2 = format_number(second_input)

                if user_choice == "1":
                    res = add_values(first_input, second_input)
                    print(f"Result: {num1} + {num2} = {format_number(res)}")
                elif user_choice == "2":
                    res = subtract_values(first_input, second_input)
                    print(f"Result: {num1} - {num2} = {format_number(res)}")
                elif user_choice == "3":
                    res = multiply_values(first_input, second_input)
                    print(f"Result: {num1} * {num2} = {format_number(res)}")
                elif user_choice == "4":
                    res = divide_values(first_input, second_input)
                    if res is None:
                        print("Error: Cannot divide by zero.")
                    else:
                        print(f"Result: {num1} / {num2} = {res}")
                elif user_choice == "5":
                    res = modulus_values(first_input, second_input)
                    if res is None:
                        print("Error: Cannot divide by zero.")
                    else:
                        print(f"Result: {num1} % {num2} = {format_number(res)}")
                elif user_choice == "6":
                    res = power_values(first_input, second_input)
                    print(f"Result: {num1} ** {num2} = {format_number(res)}")

            except ValueError:
                print("Error: Please enter valid numbers.")


if __name__ == "__main__":
    main()