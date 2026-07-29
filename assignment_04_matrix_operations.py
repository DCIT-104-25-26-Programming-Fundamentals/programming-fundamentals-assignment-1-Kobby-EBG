# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
def read_matrix(name):
    """Prompt the user for a matrix's dimensions and rows, return it as a 2D list."""
    rows = int(input(f"Enter number of rows for Matrix {name}: "))
    cols = int(input(f"Enter number of columns for Matrix {name}: "))

    matrix = []
    for i in range(rows):
        row_values = input(f"Enter row {i + 1}: ").split()
        row = [float(value) for value in row_values]

        if len(row) != cols:
            print(f"Error: Expected {cols} values, got {len(row)}. Please re-enter.")
            return read_matrix(name)  # restart input for this matrix

        matrix.append(row)

    return matrix


def print_matrix(matrix, title="Matrix"):
    """Display a matrix in a neat, aligned grid."""
    print(f"\n{title}:")
    for row in matrix:
        formatted_row = "  ".join(f"{value:g}" for value in row)
        print(formatted_row)


def transpose(matrix):
    """Return the transpose of an M x N matrix as an N x M matrix."""
    rows = len(matrix)
    cols = len(matrix[0])

    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)

    return result


def add_matrices(matrix_a, matrix_b):
    """Return the element-wise sum of two matrices of the same size."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(new_row)

    return result


def multiply_matrices(matrix_a, matrix_b):
    """Return the matrix product of A (M x N) and B (N x P) as an M x P matrix."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][j]
            new_row.append(total)
        result.append(new_row)

    return result


def part_a_transpose():
    print("\n--- Part A: Transpose a Matrix ---")
    matrix = read_matrix("")
    print_matrix(matrix, "Original Matrix")

    result = transpose(matrix)
    print_matrix(result, "Transposed Matrix")


def part_b_addition():
    print("\n--- Part B: Add Two Matrices ---")
    matrix_a = read_matrix("A")
    print_matrix(matrix_a, "Matrix A")

    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])

    print(f"\nMatrix B must be {rows_a} x {cols_a} to match Matrix A.")
    matrix_b = read_matrix("B")

    if len(matrix_b) != rows_a or len(matrix_b[0]) != cols_a:
        print("Error: Matrix B must be the same size as Matrix A.")
        return

    print_matrix(matrix_b, "Matrix B")

    result = add_matrices(matrix_a, matrix_b)
    print_matrix(result, "Sum (A + B)")


def part_c_multiplication():
    print("\n--- Part C: Multiply Two Matrices ---")
    matrix_a = read_matrix("A")
    print_matrix(matrix_a, "Matrix A")

    cols_a = len(matrix_a[0])

    print(f"\nMatrix B must have {cols_a} rows to match Matrix A's columns.")
    matrix_b = read_matrix("B")

    if len(matrix_b) != cols_a:
        print("Error: Number of rows in Matrix B must equal number of columns in Matrix A.")
        return

    print_matrix(matrix_b, "Matrix B")

    result = multiply_matrices(matrix_a, matrix_b)
    print_matrix(result, "Product (A x B)")


def main():
    print("Matrix Operations")
    print("1. Transpose a Matrix")
    print("2. Add Two Matrices")
    print("3. Multiply Two Matrices")

    choice = input("Choose an operation (1-3): ").strip()

    if choice == "1":
        part_a_transpose()
    elif choice == "2":
        part_b_addition()
    elif choice == "3":
        part_c_multiplication()
    else:
        print("Error: Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
# =============================================================================

