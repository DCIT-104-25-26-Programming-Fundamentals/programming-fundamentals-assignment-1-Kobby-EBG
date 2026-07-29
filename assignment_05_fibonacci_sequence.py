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
def generate_fibonacci(n):
    """Return a list containing the first n Fibonacci numbers, using a loop."""
    sequence = []
    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence


def print_first_n_terms():
    """Part A: Ask for N and print the first N Fibonacci terms."""
    n = int(input("How many terms? "))

    if n <= 0:
        print("Error: The number of terms must be a positive integer.")
        return

    sequence = generate_fibonacci(n)
    print("Fibonacci sequence:", " ".join(str(num) for num in sequence))


def is_fibonacci_number():
    """Part B: Ask for a number and check if it appears in the Fibonacci sequence."""
    number = int(input("Enter a number to check: "))

    if number < 0:
        print("Error: Please enter a non-negative number.")
        return

    a, b = 0, 1
    found = False

    while a <= number:
        if a == number:
            found = True
            break
        a, b = b, a + b

    if found:
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")


def main():
    print("Fibonacci Sequence Generator")
    print("1. Print the first N terms")
    print("2. Check if a number is a Fibonacci number")

    choice = input("Choose an option (1-2): ").strip()

    if choice == "1":
        print_first_n_terms()
    elif choice == "2":
        is_fibonacci_number()
    else:
        print("Error: Please enter 1 or 2.")


if __name__ == "__main__":
    main()
# =============================================================================

