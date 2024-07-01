def is_solved(board):
    not_finished = False

    for i in range(3):
        # Check row
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]
        # Check column
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]

        # Check if the game is still ongoing
        if 0 in board[i]:
            not_finished = True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]

    # If there are still empty cells, the game is not finished
    if not_finished:
        return -1

    # If no winner and no unfinished game, it's a draw
    return 0
