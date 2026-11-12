
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve_n_queens(n):
    board = [-1] * n
    solutions = []
    count = 0

    def backtrack(row):
        nonlocal count

        if row == n:
            count += 1

            if not solutions:
                solutions.append(board.copy())

            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)

    print("Total Solutions:", count)

    if solutions:
        print("One Valid Solution:")
        for row in range(n):
            for col in range(n):
                if solutions[0][row] == col:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
    else:
        print("No solution exists")


n = int(input("Enter value of N: "))

if n <= 0:
    print("Enter a positive integer")
else:
    solve_n_queens(n)
