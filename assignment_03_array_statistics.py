# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def find_sum(num_list):
    total = 0
    for n in num_list:
        total += n
    return total

def find_avg(num_list):
    return find_sum(num_list) / len(num_list)

def find_max(num_list):
    highest = num_list[0]
    for n in num_list[1:]:
        if n > highest:
            highest = n
    return highest

def find_min(num_list):
    lowest = num_list[0]
    for n in num_list[1:]:
        if n < lowest:
            lowest = n
    return lowest

def main():
    count = int(input("How many numbers? "))
    if count <= 0:
        print("Error: N must be a positive integer.")
        return

    items = []
    for i in range(1, count + 1):
        val = float(input(f"Enter number {i}: "))
        items.append(val)

    # Format numbers nicely
    clean = lambda x: int(x) if x.is_integer() else x

    print("\nResults:")
    print(f"Sum:     {clean(find_sum(items))}")
    print(f"Average: {find_avg(items)}")
    print(f"Maximum: {clean(find_max(items))}")
    print(f"Minimum: {clean(find_min(items))}")

if __name__ == "__main__":
    main()