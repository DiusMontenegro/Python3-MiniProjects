# import necessary libraries
import tkinter as tk

# define game board and other variables
board = ["", "", "", "", "", "", "", "", ""]
current_player = "X"
player1_score = 0
player2_score = 0

# create the main window
window = tk.Tk()
window.title("Tic Tac Toe")

# create the labels for displaying scores and current turn
score_label = tk.Label(window, text="Player 1: {}  Player 2: {}".format(player1_score, player2_score))
score_label.pack()
turn_label = tk.Label(window, text="Current Turn: Player {}".format(current_player))
turn_label.pack()

# create the buttons for the game board
button_frame = tk.Frame(window)
button_frame.pack()
buttons = []
for i in range(9):
    button = tk.Button(button_frame, text="", width=3, height=1, command=lambda pos=i: on_click(pos))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# define GUI functions
def on_click(position):
    global current_player
    global board
    global player1_score
    global player2_score
    if board[position] == "":
        board[position] = current_player
        update_board()
        if check_winner():
            if current_player == "X":
                player1_score += 1
            else:
                player2_score += 1
            display_winner()
            reset_game()
        elif check_tie():
            display_tie()
            reset_game()
        else:
            switch_player()

def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    display_turn()

def update_board():
    # update the GUI with the current state of the board
    for i, mark in enumerate(board):
        buttons[i].configure(text=mark)

def check_winner():
    # check for a winning combination and return True if found
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)             # diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            return True
    return False

def display_winner():
    # display a message declaring the winner and update the score
    winner = "Player 1" if current_player == "O" else "Player 2"
    score_label.configure(text="Player 1: {}  Player 2: {}".format(player1_score, player2_score))
    tk.messagebox.showinfo("Winner!", "{} wins!".format(winner))

def check_tie():
    # check if the game is tied and return True if it is
    return not "" in board

def display_tie():
    # display a message declaring a tie game
    tk.messagebox.showinfo("Tie Game!", "The game ended in a tie.")

def reset_game():
    global board
    board = ["", "", "", "", "", "", "", "", ""]
    update_board()
   

