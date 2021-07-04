from tkinter import Tk, Label, Button
import random

root = Tk()
root.config(bg="black")

current_player = None

winner = None

values = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

Xscore = 0

Oscore = 0

Total = 0

Tie = 0

p = ["X", "O"]


def Rematch():

    global winner, current_player, values, Xscore, Oscore, Total, Tie, p

    Rp = random.choice(p)

    Total += 1

    current_player = Rp

    l.config(text=current_player)

    if " " not in values:

        Tie += 1

        l6.config(text=f"TIE : {Tie}")

    if winner == "X":

        Xscore += 1

        l3.config(text=f"X : {Xscore}")

    elif winner == "O":

        Oscore += 1

        l4.config(text=f"O : {Oscore}")

    l.config(text=""), l1.config(text="", width=0, bg="black"), l2.config(
        text="", bg="black", width=0, height=0
    ), l5.config(text=f"TOTAL : {Total}")

    winner = None

    set_current_player(current_player)

    count = -1

    for i in values:

        count += 1

        values[count] = " "

    for i in buttons:

        i.config(text="")

    REMATCH.config(state="disable")
    RESTART.config(state="disable")


def Restart():

    global winner, current_player, values, Xscore, Oscore, Total, Tie

    Total = 0

    Tie = 0

    l6.config(text=f"TIE : {Tie}")

    Xscore = 0

    l3.config(text=f"X : {Xscore}")

    Oscore = 0

    l4.config(text=f"O : {Oscore}")

    for i in buttons:

        i.config(state="disable")

    O.config(state="normal"), X.config(state="normal"), l.config(text=""), l1.config(
        text="", width=0, bg="black"
    ), l2.config(text="", bg="black", width=0, height=0), l5.config(
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
    REMATCH.config(state="disable")


def passs():
    pass


def check_rows():

    row1 = values[0] == values[1] == values[2] != " "

    row2 = values[3] == values[4] == values[5] != " "

    row3 = values[6] == values[7] == values[8] != " "

    if row1:

        l1.grid(row=3, sticky="s", columnspan=3, rowspan=2, pady=140)

        return values[0]

    elif row2:

        l1.grid(row=3, sticky="s", columnspan=3, rowspan=3, pady=140)

        return values[3]

    elif row3:

        l1.grid(row=3, sticky="s", columnspan=3, rowspan=4, pady=140)

        return values[6]


def check_columns():

    column1 = values[0] == values[3] == values[6] != " "

    column2 = values[1] == values[4] == values[7] != " "

    column3 = values[2] == values[5] == values[8] != " "

    if column1:

        l2.grid(row=4, sticky="e", rowspan=3, padx=170, columnspan=1)

        return values[0]

    elif column2:

        l2.grid(row=4, sticky="e", rowspan=3, padx=173, columnspan=2)

        return values[1]

    elif column3:

        l2.grid(row=4, sticky="e", rowspan=3, padx=173, columnspan=3)

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

        l1.config(text="_", width=330, bg="white")

        winner = row_winner

    elif column_winner:

        l2.config(text="|", bg="white", width=3, height=116)

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

    l.config(text=f"{current_player}'s Turn")

    if " " not in values:

        l.config(text="It's A Tie")

        RESTART.config(state="normal")
        REMATCH.config(state="normal")

    check_for_winner()

    if winner == "X" or winner == "O":

        l.config(text=f"{winner} WON ")

        RESTART.config(state="normal")
        REMATCH.config(state="normal")

        for i in buttons:

            i.config(command=passs)


def set_current_player(Player):

    global current_player

    for i in buttons:

        i.config(state="normal")

    O.config(state="disable"), X.config(state="disable")

    current_player = Player

    l.config(text=f"{current_player}'s Turn")

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
    bd=15,
    command=lambda: set_current_player("O"),
)

X = Button(
    root,
    text="X",
    bg="black",
    fg="white",
    font=("Helvetica", 9, "bold"),
    bd=15,
    command=lambda: set_current_player("X"),
)

EXIT = Button(
    root,
    text="EXIT",
    bg="black",
    fg="white",
    font=("Helvetica", 5, "bold"),
    bd=15,
    command=root.destroy,
)

REMATCH = Button(
    root,
    text="REMATCH",
    bg="black",
    fg="white",
    font=("Helvetica", 5, "bold"),
    bd=15,
    command=Rematch,
    state="disable",
)

RESTART = Button(
    root,
    text="RESTART",
    bg="black",
    fg="white",
    font=("Helvetica", 5, "bold"),
    bd=15,
    command=Restart,
    state="disable",
)

b = Button(
    root, bg="black", width=2, font=("Helvetica", 30, "bold"), state="disable", bd=30
)

b1 = Button(
    root, bg="black", width=2, font=("Helvetica", 30, "bold"), state="disable", bd=30
)

b2 = Button(
    root, bg="black", width=2, font=("Helvetica", 30, "bold"), state="disable", bd=30
)

b3 = Button(
    root, bg="black", width=2, font=("Helvetica", 30, "bold"), state="disable", bd=30
)

b4 = Button(
    root, bg="black", width=2, font=("Helvetica", 30, "bold"), state="disable", bd=30
)

b5 = Button(
    root, bg="black", width=2, font=("Helvetica", 30, "bold"), state="disable", bd=30
)

b6 = Button(
    root, bg="black", width=2, font=("Helvetica", 30, "bold"), state="disable", bd=30
)

b7 = Button(
    root, bg="black", width=2, font=("Helvetica", 30, "bold"), state="disable", bd=30
)

b8 = Button(
    root, bg="black", width=2, font=("Helvetica", 30, "bold"), state="disable", bd=30
)


buttons = [b, b1, b2, b3, b4, b5, b6, b7, b8]


l = Label(root, fg="white", bg="black", font=("Helvetica", 15, "bold"))

l1 = Label(root, font=("Helvetica", 1, "bold"))

l2 = Label(root, font=("Helvetica", 1, "bold"))

l3 = Label(
    root, text=f"X : {Xscore}", fg="white", bg="black", font=("Helvetica", 10, "bold")
)

l4 = Label(
    root, text=f"O : {Oscore}", fg="white", bg="black", font=("Helvetica", 10, "bold")
)

l5 = Label(
    root,
    text=f"TOTAL : {Total}",
    fg="white",
    bg="black",
    font=("Helvetica", 10, "bold"),
)

l6 = Label(
    root, text=f"TIE : {Tie}", fg="white", bg="black", font=("Helvetica", 10, "bold")
)


l5.grid(column=1)
l6.grid(column=1)
l.grid(column=1, pady=70)
l3.grid(columnspan=2)
l4.grid(row=3, column=1, columnspan=2)


b.grid(row=4)
b1.grid(row=4, column=1)
b2.grid(row=4, column=2)
b3.grid(row=5)
b4.grid(row=5, column=1)
b5.grid(row=5, column=2)
b6.grid(row=6)
b7.grid(row=6, column=1)
b8.grid(row=6, column=2)

REMATCH.grid(row=8, ipadx=50, pady=50)
RESTART.grid(row=8, column=2, ipadx=50)
X.grid(row=10, columnspan=2, ipadx=50)
O.grid(row=10, column=1, columnspan=2, ipadx=50)
EXIT.grid(column=1, pady=50, ipadx=50)


root.mainloop()
