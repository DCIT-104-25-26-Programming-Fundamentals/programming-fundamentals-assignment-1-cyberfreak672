# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def make_fib_list(n_terms):
    if n_terms <= 0:
        return []
    if n_terms == 1:
        return [0]
    
    seq = [0, 1]
    for _ in range(2, n_terms):
        seq.append(seq[-1] + seq[-2])
    return seq

def check_if_fib(target):
    if target < 0:
        return False
    a, b = 0, 1
    while a < target:
        a, b = b, a + b
    return a == target

def main():
    try:
        n = int(input("How many terms? "))
        if n <= 0:
            print("Error: N must be a positive integer.")
        else:
            fib_series = make_fib_list(n)
            print("Fibonacci sequence:", " ".join(str(x) for x in fib_series))
    except ValueError:
        print("Error: N must be a positive integer.")

    print()

    try:
        val = int(input("Enter a number to check: "))
        if check_if_fib(val):
            print(f"{val} is a Fibonacci number.")
        else:
            print(f"{val} is NOT a Fibonacci number.")
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    main()