board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def print_board(board):
    print("---+---+---")
    for row in board:
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        print("---+---+---")


print_board(board)


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != " ":
            return True

    if (
        board[0][0] == board[1][1] == board[2][2] != " "
        or board[2][2] == board[1][1] == board[0][0] != " "
    ):
        return True

    return False


print(check_winner(board))
