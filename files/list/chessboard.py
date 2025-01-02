def board_setup():
    """
    Creates a chess board represented as an 8x8 grid.
    Each cell is initialized with 'x' to indicate an empty cell.
    """
    board = []
    empty = 'x'

    for _ in range(8):  # Use '_' for loop variables when the value isn't needed
        row = [empty for _ in range(8)]
        board.append(row)

    return board  # Return the board


def chess_pieces(empty_board):
    """
    Populates the chessboard with initial pieces.
    Adds rooks, a knight, and a pawn as an example setup.
    """
    ROOK = 'r'
    KNIGHT = 'k'
    PAWN = 'p'

    # Place rooks
    empty_board[0][0] = ROOK
    empty_board[0][7] = ROOK
    empty_board[7][0] = ROOK
    empty_board[7][7] = ROOK

    # Place a knight
    empty_board[4][2] = KNIGHT

    # Place a pawn
    empty_board[3][4] = PAWN

    return empty_board


# Call the function to create an empty chessboard
smt = board_setup()

# Display the empty board in a readable format
print("Empty Chess Board:")
for row in smt:
    print(" ".join(row))


# Populate the chessboard with pieces
board_pieces = chess_pieces(smt)

# Display the board with pieces
print("\nChess Board with Pieces:")
for row in board_pieces:
    print(" ".join(row))
