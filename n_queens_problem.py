n_of_queens = 8
board = []


def is_valid_column(j):
    for i in range(n_of_queens):
        if(board[i][j] == 1):
            return False

    return True


def is_valid_row(i):
    for j in range(n_of_queens):
        if(board[i][j] == 1):
            return False

    return True


def is_valid_diagonal(i, j):
    for i, j in zip(range(i, -1, -1), range(j, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(i, n_of_queens, 1), range(j, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def is_valid(i, j):
    return is_valid_column(j) and is_valid_row(i) and is_valid_diagonal(i, j)


def solve(j=0):
    if(j == n_of_queens):
        return board

    for k in range(n_of_queens):
        if(is_valid(k, j)):
            board[k][j] = 1
            if(solve(j+1)):
                return True

            board[k][j] = 0

    return False


def start():
    for i in range(n_of_queens):
        temp = []
        for j in range(n_of_queens):
            temp.append(0)

        board.append(temp)

    return solve()


start()
for line in board:
    print(line)
