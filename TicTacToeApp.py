import tkinter as tk
from PIL import Image, ImageTk


def player_turn(reverse=None) -> str:
    global x_turn

    temp_bool = x_turn

    if reverse is not None and reverse is True:
        temp_bool = not temp_bool

    if temp_bool:
        return "X"
    else:
        return "O"


def player_color():
    if x_turn:
        return "red"
    else:
        return "blue"


def player_image():
    if x_turn:
        return button_x_image
    else:
        return button_o_image


def restart():
    for button_row in buttons:
        for button in button_row:
            button.config(text="", image="", state="normal")
    game_message["text"] = "Click a square to begin"
    play_again.pack_forget()


def close_app():
    window.destroy()


def update_button_status(row, col):
    global x_turn
    buttons[row][col].config(text=player_turn(), fg=player_color(), image=player_image(), state="disabled")
    win_condition(row, col)
    x_turn = not x_turn


def win_condition(row, col):
    if won_row(col) or won_col(row) or won_diag(row, col):
        game_message["text"] = player_turn(), "WON!!!"

        for button_row in buttons:
            for button in button_row:
                button["state"] = "disabled"

        play_again.pack(side=tk.LEFT, expand=25)
    elif tie_condition():
        game_message["text"] = "TIE"
        play_again.pack(side=tk.LEFT, expand=25)
    else:
        game_message["text"] = player_turn(True) + "'s turn"


def won_row(col) -> bool:
    counter = 0

    for button_row in buttons:
        if button_row[col]["text"] == player_turn():
            counter += 1

    if counter >= 3:
        return True
    else:
        return False


def won_col(row) -> bool:
    counter = 0

    for button in buttons[row]:
        if button["text"] == player_turn():
            counter += 1

    if counter >= 3:
        return True
    else:
        return False


def won_diag(row, col) -> bool:
    counter = 0

    for i in range(0, len(buttons)):
        if buttons[i][i]["text"] == player_turn():
            counter += 1

    if counter >= 3:
        return True
    else:
        counter = 0

    for i in range(0, len(buttons)):
        if buttons[i][len(buttons) - 1 - i]["text"] == player_turn():
            counter += 1

    if counter >= 3:
        return True
    else:
        return False


def tie_condition() -> bool:
    counter = 0
    for button_row in buttons:
        for button in button_row:
            if button["text"] == "X" or button["text"] == "O":
                counter += 1

    if counter == 9:
        return True
    else:
        return False


def idle_message():
    game_message["text"] = "EY EY EY LOOKIE HERE"


buttons = [[None] * 3 for x in range(3)]
x_turn = True

window = tk.Tk()
window.title("TicTacToe - AR")
window.configure(bg="teal", borderwidth=25, relief="groove")
window.iconbitmap("TicTacToeXAndOImage.ico")

# GAME FRAME INITIALIZATION
frame1 = tk.Frame()
frame1.rowconfigure([0, 1, 2], minsize=75, weight=1)
frame1.columnconfigure([0, 1, 2], minsize=75, weight=1)
frame1.pack()

for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(master=frame1, text=" ", bg="black", fg="white", relief="raised", border=5,
                                      command=lambda row=row, col=col: update_button_status(row, col))
        buttons[row][col].grid(row=row, column=col, sticky="nsew")

button_x_image = ImageTk.PhotoImage(Image.open("x_image.png").resize((50, 50)))
button_o_image = ImageTk.PhotoImage(Image.open("o_image.png").resize((50, 50)))

# MESSAGE TEXT (UNDER)
frame2 = tk.Frame(borderwidth=15, relief="raised", bg="teal")
frame2.pack()

game_message = tk.Label(master=frame2, text="Click a square to begin", font="georgia", width=25, bg="teal",
                        relief="solid")
game_message.pack()

play_again = tk.Button(text="Play again?", command=restart, width=8, bg="black", fg="white", relief="raised", border=3)
close_app_button = tk.Button(text="Exit", command=close_app, width=8, bg="black", fg="white", relief="raised", border=3)
close_app_button.pack(side=tk.RIGHT, expand=25)

window.mainloop()
