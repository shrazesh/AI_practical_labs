print("      N Queens constraint Satisfaction problem.       ")
def print_solution(board):
    """Prints the board in a readable format."""
    for row in board:
        print(" ".join("Q" if cell else "_" for cell in row))
    print("\n")

def is_safe(board, row, col, n):
    """Checks if placing a queen at board[row][col] is safe."""
    # Check the left side of the row
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def solve_n_queens_util(board, col, n):
    """Utilizes backtracking to solve the N-Queens problem."""
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            # Place the queen
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solve_n_queens_util(board, col + 1, n):
                return True

            # Backtrack
            board[i][col] = 0

    return False

def solve_n_queens(n):
    """Main function to solve the N-Queens problem."""
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print("No solution exists for N =", n)
    else:
        print("Solution for N =", n)
        print_solution(board)

if __name__ == "__main__":
    try:
        n = int(input("Enter the value of N (size of the chessboard): "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            solve_n_queens(n)
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
