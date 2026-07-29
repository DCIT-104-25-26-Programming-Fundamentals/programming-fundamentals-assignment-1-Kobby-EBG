# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
def print_table(number):
    """Print the multiplication table for a single number, from 1 to 12."""
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number}  x  {i:<2} =  {number * i}")


def part_a_single_table():
    """Part A: Ask for a number and print its multiplication table."""
    number = int(input("Enter a number: "))
    print_table(number)


def part_b_tables_up_to_n():
    """Part B: Ask for N and print multiplication tables from 1 to N."""
    n = int(input("Enter N: "))

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    for number in range(1, n + 1):
        print_table(number)
        if number != n:
            print("-" * 29)


def main():
    print("Multiplication Table Generator")
    print("1. Single table")
    print("2. Tables from 1 to N")

    choice = input("Choose an option (1-2): ").strip()

    if choice == "1":
        part_a_single_table()
    elif choice == "2":
        part_b_tables_up_to_n()
    else:
        print("Error: Please enter 1 or 2.")


if __name__ == "__main__":
    main()
# =============================================================================

