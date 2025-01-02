import random

# Function to print the board in the required format
def print_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

# Function to create a new board
def create_board():
    return [[str(i + 1 + j * 3) for i in range(3)] for j in range(3)]

# Function to check for free squares
def make_list_of_free_fields(board):
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j].isdigit():
                free_fields.append((i, j))
    return free_fields

# Function to check if there is a victory for a player
def victory_for(board, sign):
    # Check rows, columns, and diagonals for a victory
    for i in range(3):
        if all([board[i][j] == sign for j in range(3)]) or \
           all([board[j][i] == sign for j in range(3)]):
            return True
    if (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) or \
       (board[0][2] == sign and board[1][1] == sign and board[2][0] == sign):
        return True
    return False

# Function for the computer to make a random move
def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    row, col = random.choice(free_fields)
    board[row][col] = 'X'

# Main game loop
def play_game():
    board = create_board()
    print_board(board)
    
    while True:
        # Player's move
        valid_move = False
        while not valid_move:
            try:
                player_move = int(input("Enter your move (1-9): ")) - 1
                row, col = divmod(player_move, 3)
                if board[row][col].isdigit():
                    board[row][col] = 'O'
                    valid_move = True
                else:
                    print("This square is already taken!")
            except (ValueError, IndexError):
                print("Invalid input! Please enter a number between 1 and 9.")

        print_board(board)

        # Check if the player has won
        if victory_for(board, 'O'):
            print("You won!")
            break

        # Check if the board is full (tie)
        if not make_list_of_free_fields(board):
            print("It's a tie!")
            break

        # Computer's move
        draw_move(board)
        print_board(board)

        # Check if the computer has won
        if victory_for(board, 'X'):
            print("Computer wins!")
            break

        # Check if the board is full (tie)
        if not make_list_of_free_fields(board):
            print("It's a tie!")
            break

# Run the game
play_game()
