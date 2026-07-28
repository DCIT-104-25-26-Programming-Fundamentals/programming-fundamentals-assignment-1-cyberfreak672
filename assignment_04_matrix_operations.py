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
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_matrix(matrix):
    """Prints a matrix in a neat grid format."""
    for row in matrix:
        print(" ".join(str(val) for val in row))


def read_matrix(rows, cols, name="Matrix"):
    """Helper function to read a matrix from user input."""
    matrix = []
    for i in range(1, rows + 1):
        row = list(map(int, input(f"Enter row {i}: ").split()))
        matrix.append(row)
    return matrix


def transpose_matrix(matrix):
    """Computes the transpose of an M x N matrix."""
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []

    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        transposed.append(new_row)

    return transposed


def add_matrices(matrix1, matrix2):
    """Adds two M x N matrices element-wise."""
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = []

    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(matrix1[r][c] + matrix2[r][c])
        result.append(row)

    return result


def multiply_matrices(matrix_a, matrix_b):
    """Multiplies an M x N matrix A by an N x P matrix B."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    # Resulting matrix is size M x P
    result = []
    for r in range(rows_a):
        row = []
        for c in range(cols_b):
            # Compute dot product for position (r, c)
            dot_product = 0
            for k in range(cols_a):
                dot_product += matrix_a[r][k] * matrix_b[k][c]
            row.append(dot_product)
        result.append(row)

    return result


def main():
    print("=== PART A: Transpose Matrix ===")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    matrix_a = read_matrix(m, n)

    print("\nOriginal Matrix:")
    print_matrix(matrix_a)

    print("\nTransposed Matrix:")
    print_matrix(transpose_matrix(matrix_a))

    print("\n=== PART B: Add Two Matrices ===")
    print(f"Enter Matrix B (must be {m} x {n}):")
    matrix_b = read_matrix(m, n)

    print("\nSum of Matrices:")
    print_matrix(add_matrices(matrix_a, matrix_b))

    print("\n=== PART C: Multiply Two Matrices ===")
    p = int(input(f"Enter number of columns for Matrix C (Matrix B is {n} x P): "))
    print(f"Enter Matrix C ({n} x {p}):")
    matrix_c = read_matrix(n, p)

    print("\nMatrix Product (A x C):")
    print_matrix(multiply_matrices(matrix_a, matrix_c))


if __name__ == "__main__":
    main()