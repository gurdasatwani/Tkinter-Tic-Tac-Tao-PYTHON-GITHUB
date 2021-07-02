# ------------------MODULES------------------------

from tkinter import Tk, Label, Button

# -----------------------------------------------------

root = Tk()


root.config(bg="black")

# ----------------------BASE2------------------‐-----

# 										(DONE)

# 1). CURRENT PLAYER   = NONE

current_player = None

# 2). WINNER OR TIE 	   = NONE

winner = None

# -----------------------------------------------------

values = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def Restart():
    global winner, current_player, values
    for i in buttons:
        i.config(state="disable")
    O.config(state="normal"), X.config(state="normal")
    l4.config(text="")
    winner = None
    current_player = None
    count = -1
    for i in values:
        count += 1
        values[count] = " "
    for i in buttons:
        i.config(text="")

    RESTART.config(state="disable")


def passs():
    pass


def check_rows():

    row1 = values[0] == values[1] == values[2] != " "

    row2 = values[3] == values[4] == values[5] != " "

    row3 = values[6] == values[7] == values[8] != " "

    if row1:

        return values[0]

    elif row2:

        return values[3]

    elif row3:

        return values[6]


def check_columns():

    column1 = values[0] == values[3] == values[6] != " "

    column2 = values[1] == values[4] == values[7] != " "

    column3 = values[2] == values[5] == values[8] != " "

    if column1:

        return values[0]

    elif column2:

        return values[1]

    elif column3:

        return values[2]


def check_diagonals():

    diagonal1 = values[0] == values[4] == values[8] != " "

    diagonal2 = values[2] == values[4] == values[6] != " "

    if diagonal1:

        return values[0]

    elif diagonal2:

        return values[2]


def check_for_winner():

    global winner

    row_winner = check_rows()

    column_winner = check_columns()

    diagonal_winner = check_diagonals()

    if row_winner:

        winner = row_winner

    elif column_winner:

        winner = column_winner

    elif diagonal_winner:

        winner = diagonal_winner


def Turn(Button, Position):

    global current_player

    if current_player == "X":

        if values[Position] == " ":

            values[Position] = current_player

            Button.config(command=passs, state="disable")

        Button.config(text=current_player, fg="yellow", state="normal")

        current_player = "O"

    elif current_player == "O":

        if values[Position] == " ":

            values[Position] = current_player

            Button.config(command=passs, state="disable")

        Button.config(text=current_player, fg="orange", state="normal")

        current_player = "X"

    l4.config(text=f"{current_player}'s Turn")

    if " " not in values:
        l4.config(text="It's A Tie")
        RESTART.config(state="normal")

    check_for_winner()

    if winner == "X" or winner == "O":

        l4.config(text=f"{winner} WON ")

        RESTART.config(state="normal")

        for i in buttons:
            i.config(command=passs)

        RESTART.place(x=420, y=1800)


def set_current_player(Player):

    global current_player

    for i in buttons:
        i.config(state="normal")

    O.config(state="disable"), X.config(state="disable")

    current_player = Player

    l4.config(text=f"{current_player}'s Turn")

    b.config(command=lambda: Turn(b, 0)), b1.config(
        command=lambda: Turn(b1, 1)
    ), b2.config(command=lambda: Turn(b2, 2)), b3.config(
        command=lambda: Turn(b3, 3)
    ), b4.config(
        command=lambda: Turn(b4, 4)
    ), b5.config(
        command=lambda: Turn(b5, 5)
    ), b6.config(
        command=lambda: Turn(b6, 6)
    ), b7.config(
        command=lambda: Turn(b7, 7)
    ), b8.config(
        command=lambda: Turn(b8, 8)
    )


O = Button(
    root,
    text="O",
    bg="black",
    fg="white",
    font=("Helvetica", 9, "bold"),
    bd=10,
    command=lambda: set_current_player("O"),
)


X = Button(
    root,
    text="X",
    bg="black",
    fg="white",
    font=("Helvetica", 9, "bold"),
    bd=10,
    command=lambda: set_current_player("X"),
)

EXIT = Button(
    root,
    text="EXIT",
    bg="black",
    fg="white",
    font=("Helvetica", 5, "bold"),
    bd=10,
    command=root.destroy,
)
RESTART = Button(
    root,
    text="RESTART",
    bg="black",
    fg="white",
    font=("Helvetica", 5, "bold"),
    bd=10,
    command=Restart,
)


b = Button(
    root,
    bg="black",
    width=2,
    font=("Helvetica", 40, "bold"),
    state="disable",
)

b1 = Button(
    root,
    bg="black",
    width=2,
    font=("Helvetica", 40, "bold"),
    state="disable",
)

b2 = Button(
    root,
    bg="black",
    width=2,
    font=("Helvetica", 40, "bold"),
    state="disable",
)

b3 = Button(
    root,
    bg="black",
    width=2,
    font=("Helvetica", 40, "bold"),
    state="disable",
)

b4 = Button(
    root,
    bg="black",
    width=2,
    font=("Helvetica", 40, "bold"),
    state="disable",
)

b5 = Button(
    root,
    bg="black",
    width=2,
    font=("Helvetica", 40, "bold"),
    state="disable",
)


b6 = Button(
    root,
    bg="black",
    width=2,
    font=("Helvetica", 40, "bold"),
    state="disable",
)


b7 = Button(
    root,
    bg="black",
    width=2,
    font=("Helvetica", 40, "bold"),
    state="disable",
)


b8 = Button(
    root,
    bg="black",
    width=2,
    font=("Helvetica", 40, "bold"),
    state="disable",
)


l2 = Label(
    root, text="_", fg="white", bg="white", font=("Helvetica", 1, "bold"), width=355
)

l3 = Label(
    root, text="_", fg="white", bg="white", font=("Helvetica", 1, "bold"), width=355
)

l = Label(
    root, text="|", fg="white", bg="white", font=("Helvetica", 1, "bold"), height=134
)

l1 = Label(
    root, text="|", fg="white", bg="white", font=("Helvetica", 1, "bold"), height=134
)


l4 = Label(root, fg="white", bg="black", font=("Helvetica", 15, "bold"))

buttons = [b, b1, b2, b3, b4, b5, b6, b7, b8]


O.place(x=645, y=1640)
X.place(x=278, y=1640)
EXIT.place(x=450, y=1500)
b.place(y=490)
b1.place(x=360, y=490)
b2.place(x=710, y=490)


b3.place(y=810)
b4.place(x=360, y=810)
b5.place(x=710, y=810)


b6.place(y=1130)
b7.place(x=360, y=1130)
b8.place(x=710, y=1130)


l.place(x=355, y=490)
l1.place(x=710, y=490)
l2.place(y=795)
l3.place(y=1115)
l4.place(x=370, y=200)


root.mainloop()
