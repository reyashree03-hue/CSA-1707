def solve_n_queens(board, row):
    n = 8

    if row == n:
        for r in board:
            print(" ".join("Q" if x else "." for x in r))
        print()
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve_n_queens(board, row + 1):
                return True

            board[row][col] = 0

    return False


def is_safe(board, row, col):
    n = 8

    for i in range(row):
        if board[i][col]:
            return False

        if col - (row - i) >= 0:
            if board[i][col - (row - i)]:
                return False

        if col + (row - i) < n:
            if board[i][col + (row - i)]:
                return False

    return True


board = [[0 for _ in range(8)] for _ in range(8)]

if not solve_n_queens(board, 0):
    print("No solution found")
