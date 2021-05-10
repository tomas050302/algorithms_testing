n_of_queens = 8


def is_valid_column(board, j):
    for i in range(n_of_queens):
        if(board[i][j] == 1):
            return False

    return True


def is_valid_row(board, i):
    for j in range(n_of_queens):
        if(board[i][j] == 1):
            return False

    return True


def is_valid_diagonal(board, i, j):
    if(i > j):
        for x in range(n_of_queens-i):
            if(board[i+x][j+x] == 1):
                return False
    else:
        for x in range(n_of_queens-j):
            if(board[i+x][j+x] == 1):
                return False

    return True


def is_valid(board, i, j):
    return is_valid_column(board, j) and is_valid_row(board, i) and is_valid_diagonal(board, i, j)


def solve(board, i, j, placed):
    if(placed == n_of_queens):
        return board

    for k in range(n_of_queens):
        print(board)
        if(is_valid(board, i, k)):
            board[i][k] = 1
            return solve(board, i+1, j, placed+1)
        board[i][k] = 0


def start():
    board = []
    for i in range(n_of_queens):
        temp = []
        for j in range(n_of_queens):
            temp.append(0)

        board.append(temp)

    return solve(board, i, j, 0)


print(start())
