# ==========================================
#           Tic Tac Toe - Python
# ==========================================

# 3x3 board represented as a 2D list; "-" marks an empty cell
board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

game_still_going = True   # Tracks whether the game is still in progress
winner = None             # Stores the winning player ("X" or "O"), or None for a tie
current_player = "X"      # X always goes first


# ==========================================
#              Game Flow
# ==========================================

def play_game():
    """Run the main game loop until there's a winner or a tie."""
    display_board()

    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    # Announce the result
    if winner in ("X", "O"):
        print(f"{winner} won!")
    else:
        print("It's a tie!")


# ==========================================
#            Display & Input
# ==========================================

def display_board():
    """Print the current board state alongside a position reference guide."""
    print("\n")
    print(board[0][0] + " | " + board[0][1] + " | " + board[0][2] + "     1 | 2 | 3")
    print(board[1][0] + " | " + board[1][1] + " | " + board[1][2] + "     4 | 5 | 6")
    print(board[2][0] + " | " + board[2][1] + " | " + board[2][2] + "     7 | 8 | 9")
    print("\n")


def handle_turn(player):
    """Prompt the current player to pick a valid, unoccupied position, then place their mark."""
    print(f"{player}'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:
        # Re-prompt until the input is a digit between 1 and 9
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        # Convert 1-based input to 2D board coordinates
        index = int(position) - 1
        row, col = divmod(index, 3)

        # Accept the move only if the cell is empty
        if board[row][col] == "-":
            valid = True
        else:
            print("That spot is taken. Choose another position.")
            position = input("Choose a position from 1-9: ")

    # Place the player's mark on the board
    row, col = divmod(int(position) - 1, 3)
    board[row][col] = player
    display_board()


# ==========================================
#           Win / Tie Detection
# ==========================================

def check_if_game_over():
    """Check whether the game has ended by a win or a tie."""
    check_for_winner()
    check_for_tie()


def check_for_winner():
    """Determine if any player has won and update the global winner variable."""
    global winner
    winner = check_rows() or check_columns() or check_diagonals()


def check_rows():
    """Return the winning player if any row is filled with the same mark, else None."""
    global game_still_going
    for row in board:
        if row[0] == row[1] == row[2] != "-":
            game_still_going = False
            return row[0]
    return None


def check_columns():
    """Return the winning player if any column is filled with the same mark, else None."""
    global game_still_going
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "-":
            game_still_going = False
            return board[0][col]
    return None


def check_diagonals():
    """Return the winning player if either diagonal is filled with the same mark, else None."""
    global game_still_going
    # Top-left to bottom-right
    if board[0][0] == board[1][1] == board[2][2] != "-":
        game_still_going = False
        return board[0][0]
    # Top-right to bottom-left
    if board[0][2] == board[1][1] == board[2][0] != "-":
        game_still_going = False
        return board[0][2]
    return None


def check_for_tie():
    """End the game as a tie if no empty cells remain."""
    global game_still_going
    if not any("-" in row for row in board):
        game_still_going = False
        return True
    return False


# ==========================================
#            Player Management
# ==========================================

def flip_player():
    """Switch the active player from X to O, or O to X."""
    global current_player
    current_player = "O" if current_player == "X" else "X"


# ==========================================
#               Start Game
# ==========================================

play_game()