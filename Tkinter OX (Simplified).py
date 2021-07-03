from tkinter import Tk, Label, Button

root = Tk()

root.config(bg="black")

current_player = None

winner = None

values = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

Xscore = 0

Oscore = 0

Total = 0

Tie = 0


def Restart():

    global winner, current_player, values, Xscore, Oscore, Total, Tie

    Total += 1

    if " " not in values:

        Tie += 1

        l10.config(text=f"TIE : {Tie}")

    if winner == "X":

        Xscore += 1

        l7.config(text=f"X : {Xscore}")

    elif winner == "O":

        Oscore += 1

        l8.config(text=f"O : {Oscore}")

    for i in buttons:

        i.config(state="disable")

    O.config(state="normal"), X.config(state="normal"), l4.config(text=""), l5.config(
        text="", width=0, bg="black"
    ), l6.config(text="", bg="black", width=0, height=0), l9.config(
        text=f"TOTAL : {Total}"
    )

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

        l5.place(x=50, y=630)

        return values[0]

    elif row2:

        l5.place(x=50, y=950)

        return values[3]

    elif row3:

        l5.place(x=50, y=1270)

        return values[6]


def check_columns():

    column1 = values[0] == values[3] == values[6] != " "

    column2 = values[1] == values[4] == values[7] != " "

    column3 = values[2] == values[5] == values[8] != " "

    if column1:

        l6.place(x=175, y=535)

        return values[0]

    elif column2:

        l6.place(x=535, y=535)

        return values[1]

    elif column3:

        l6.place(x=885, y=535)

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

        l5.config(text="_", width=320, bg="white")

        winner = row_winner

    elif column_winner:

        l6.config(text="|", bg="white", width=3, height=120)

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

        RESTART.place(x=415, y=1500)

    check_for_winner()

    if winner == "X" or winner == "O":

        l4.config(text=f"{winner} WON ")

        RESTART.config(state="normal")

        for i in buttons:

            i.config(command=passs)

        RESTART.place(x=415, y=1500)


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


l = Label(
    root, text="|", fg="white", bg="white", font=("Helvetica", 1, "bold"), height=134
)

l1 = Label(
    root, text="|", fg="white", bg="white", font=("Helvetica", 1, "bold"), height=134
)

l2 = Label(
    root, text="_", fg="white", bg="white", font=("Helvetica", 1, "bold"), width=355
)

l3 = Label(
    root, text="_", fg="white", bg="white", font=("Helvetica", 1, "bold"), width=355
)


l4 = Label(root, fg="white", bg="black", font=("Helvetica", 15, "bold"))

l5 = Label(root, font=("Helvetica", 1, "bold"))

l6 = Label(root, font=("Helvetica", 1, "bold"))

l7 = Label(
    root, text=f"X : {Xscore}", fg="white", bg="black", font=("Helvetica", 10, "bold")
)

l8 = Label(
    root, text=f"O : {Oscore}", fg="white", bg="black", font=("Helvetica", 10, "bold")
)

l9 = Label(
    root,
    text=f"TOTAL : {Total}",
    fg="white",
    bg="black",
    font=("Helvetica", 10, "bold"),
)

l10 = Label(
    root, text=f"TIE : {Tie}", fg="white", bg="black", font=("Helvetica", 10, "bold")
)

buttons = [b, b1, b2, b3, b4, b5, b6, b7, b8]


O.place(x=645, y=1640)
X.place(x=278, y=1640)
EXIT.place(x=445, y=1800)
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
l7.place(x=300, y=350)
l8.place(x=650, y=350)
l9.pack()
l10.pack()

root.mainloop()
