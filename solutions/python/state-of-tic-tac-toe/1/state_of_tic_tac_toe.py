def gamestate(board):
    """
    Determine whether a tic-tac-toe game is won, drawn, or ongoing.
    Args:
        board (list[str]): The current tic-tac-toe board.
    Returns:
        str: "win", "draw", or "ongoing"
    Raises:
        ValueError: If the board represents an impossible game.
    """
    os = []
    xs = []
    for row_index in range(len(board)):
        for column_index in range(len(board[row_index])):
            if board[row_index][column_index] == "X":
                xs.append((row_index, column_index))
            elif board[row_index][column_index] == "O":
                os.append((row_index, column_index))
    if len(xs) < len(os):
        raise ValueError("Wrong turn order: O started")
    if len(xs) > len(os) + 1:
        raise ValueError("Wrong turn order: X went twice")
    winning_combinations = [
        # Rows
        {(0, 0), (0, 1), (0, 2)},
        {(1, 0), (1, 1), (1, 2)},
        {(2, 0), (2, 1), (2, 2)},

        # Columns
        {(0, 0), (1, 0), (2, 0)},
        {(0, 1), (1, 1), (2, 1)},
        {(0, 2), (1, 2), (2, 2)},

        # Diagonals
        {(0, 0), (1, 1), (2, 2)},
        {(0, 2), (1, 1), (2, 0)},
    ]
    xs = set(xs)
    os = set(os)
    x_wins = False
    o_wins = False
    for combination in winning_combinations:
        if combination.issubset(xs):
            x_wins = True
        if combination.issubset(os):
            o_wins = True
    if x_wins and o_wins:
        raise ValueError("Impossible board: game should have ended after the game was won")
    if x_wins and len(xs) != len(os) + 1:
        raise ValueError("Impossible board: game should have ended after the game was won")
    if o_wins and len(xs) != len(os):
        raise ValueError("Impossible board: game should have ended after the game was won")
    if x_wins or o_wins:
        return "win"
    if len(xs) + len(os) == 9:
        return "draw"
    return "ongoing"