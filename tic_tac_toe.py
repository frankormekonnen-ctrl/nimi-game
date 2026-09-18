# Tic-Tac-Toe Game
# Player 1 = X
# Player 2 = O


# The board is a list of 9 boxes.
# At the start each box shows its own number.
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def show_board():
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


def reset_board():
    for i in range(9):
        board[i] = str(i + 1)


def is_taken(spot):
    if board[spot] == "X" or board[spot] == "O":
        return True
    else:
        return False


def take_turn(player):
    while True:
        choice = input("Player " + player + ", pick a position (1-9): ")

        if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Please type a number from 1 to 9.")
        else:
            spot = int(choice) - 1

            if is_taken(spot) == True:
                print("That position is already taken. Pick another one.")
            else:
                board[spot] = player
                break


def check_winner(player):
    # three in a row
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    elif board[3] == player and board[4] == player and board[5] == player:
        return True
    elif board[6] == player and board[7] == player and board[8] == player:
        return True
    # three in a column
    elif board[0] == player and board[3] == player and board[6] == player:
        return True
    elif board[1] == player and board[4] == player and board[7] == player:
        return True
    elif board[2] == player and board[5] == player and board[8] == player:
        return True
    # three in a diagonal
    elif board[0] == player and board[4] == player and board[8] == player:
        return True
    elif board[2] == player and board[4] == player and board[6] == player:
        return True
    else:
        return False


def check_draw():
    for i in range(9):
        if is_taken(i) == False:
            return False
    return True


# ---------- the game starts here ----------

print("Welcome to Tic-Tac-Toe!")
print("Player 1 is X and Player 2 is O.")

playing = True

while playing == True:
    reset_board()
    player = "X"
    game_over = False

    while game_over == False:
        show_board()
        take_turn(player)

        if check_winner(player) == True:
            show_board()
            print("Player " + player + " wins! Congratulations!")
            game_over = True
        elif check_draw() == True:
            show_board()
            print("It's a draw!")
            game_over = True
        else:
            # switch to the other player
            if player == "X":
                player = "O"
            else:
                player = "X"

    answer = input("Do you want to play again? (y/n): ")

    if answer == "y" or answer == "Y":
        playing = True
    else:
        playing = False
        print("Thanks for playing!")
