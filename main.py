# Global variables

# game board
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

# If game is still going
game_still_going = True

# won or tie???
winner = None

# whose turn is it??
current_player = "X"


# display board
def display_board():
    print(board[0] + " || " + board[1] + " || " + board[2])
    print(board[3] + " || " + board[4] + " || " + board[5])
    print(board[6] + " || " + board[7] + " || " + board[8])
    print("\n")


# FUNCTIONS

# Tic-Tac-Toe game
def play_game():
    # display initial board
    display_board()

    # while the game is still going
    while game_still_going:
        # handle a single turn of a arbitrary player
        handle_turn(current_player)

        # check if the game ended
        Check_if_game_over()

        # flip to the other player
        flip_player()

    # Game has ended
    if winner == "X" or winner == "O":
        print(winner + " won...")
    elif winner == None:
        print("Match Tie...")


def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose any position between 1 to 9 positions: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose the right one : ")

        position = int(position) - 1

        if board[position] == "_":
            valid = True
        else:
            print("sorry, but it was already taken")

    board[position] = player
    display_board()


def Check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    # set up global variable
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    global game_still_going
    # check in on row
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"

    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    global game_still_going
    # check in on row
    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"

    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    global game_still_going
    # check in on row
    diagonal_1 = board[0] == board[4] == board[8] != "_"
    diagonal_2 = board[2] == board[4] == board[6] != "_"

    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return


def check_if_tie():
    global game_still_going
    if "_" not in board:
        game_still_going = False
    return


def flip_player():
    # global variables we need
    global current_player
    # Changing to X if it is O and vice-versa
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


play_game()

# board
# display board
# play game
# handle turn
# check win
# check rows
# check columns
# check diagonals
# check tie
# flip player