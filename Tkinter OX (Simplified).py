from tkinter import Tk, Label, Button
import random

root = Tk()
root.config(bg="black")

current_player = None

winner = None

values = [" "]*9

Xscore = 0

Oscore = 0

Total = 0

Tie = 0

p = ["X", "O"]

ln = [f"TOTAL : {Total}", f"TIE : {Tie}", f"X : {Xscore}", f"O : {Oscore}"]

label = []

button = []

x, y = -1, -1


def Rematch():

    global winner, current_player, values, Xscore, Oscore, Total, Tie, p

    Rp = random.choice(p)

    Total += 1

    current_player = Rp

    l.config(text=current_player)

    if " " not in values:

        Tie += 1

        label[1].config(text=f"TIE : {Tie}")

    if winner == "X":

        Xscore += 1

        label[2].config(text=f"X : {Xscore}")

    elif winner == "O":

        Oscore += 1

        label[3].config(text=f"O : {Oscore}")

    for i in range(4, 6):
        
        label[i].config(text="", bg="black", width=0, height=0)

    l.config(text="")
    
    label[0].config(text=f"TOTAL : {Total}")

    winner = None

    set_current_player(current_player)

    count = -1

    for i in values:

        count += 1

        values[count] = " "

    for i in range(9):

        button[i].config(text="")

    button[10].config(state="disable")
    button[11].config(state="disable")


def Restart():

    global winner, current_player, values, Xscore, Oscore, Total, Tie

    Total = 0

    Tie = 0

    Xscore = 0

    Oscore = 0

    for i in range(4):
        
        label[i].config(text=ln[i])

    for i in range(9):

        button[i].config(text="", state="disable")

    for i in range(12, 14):
        
        button[i].config(state="normal")

    for i in range(4, 6):
        
        label[i].config(text="", bg="black", width=0, height=0)
        
    l.config(text="")

    winner = None

    current_player = None

    count = -1

    for i in values:

        count += 1

        values[count] = " "

    button[10].config(state="disable")
    button[11].config(state="disable")


def check_rows():

    row1 = values[0] == values[1] == values[2] != " "

    row2 = values[3] == values[4] == values[5] != " "

    row3 = values[6] == values[7] == values[8] != " "

    if row1:

        label[4].grid(row=3, sticky="s", columnspan=3, rowspan=2, pady=140)

        return values[0]

    elif row2:

        label[4].grid(row=3, sticky="s", columnspan=3, rowspan=3, pady=140)

        return values[3]

    elif row3:

        label[4].grid(row=3, sticky="s", columnspan=3, rowspan=4, pady=140)

        return values[6]


def check_columns():

    column1 = values[0] == values[3] == values[6] != " "

    column2 = values[1] == values[4] == values[7] != " "

    column3 = values[2] == values[5] == values[8] != " "

    if column1:

        label[5].grid(row=4, sticky="e", rowspan=3, padx=170, columnspan=1)

        return values[0]

    elif column2:

        label[5].grid(row=4, sticky="e", rowspan=3, padx=173, columnspan=2)

        return values[1]

    elif column3:

        label[5].grid(row=4, sticky="e", rowspan=3, padx=173, columnspan=3)

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

        label[4].config(text="_", width=330, bg="white")

        winner = row_winner

    elif column_winner:

        label[5].config(text="|", bg="white", width=3, height=116)

        winner = column_winner

    elif diagonal_winner:

        winner = diagonal_winner


def passs():
    pass


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

        button[10].config(state="normal")
        button[11].config(state="normal")

    check_for_winner()

    if winner == "X" or winner == "O":

        l.config(text=f"{winner} WON ")

        button[10].config(state="normal")
        button[11].config(state="normal")

        for i in range(9):

            button[i].config(command=passs)


def set_current_player(Player):

    global current_player

    for i in range(9):

        button[i].config(state="normal", command=lambda i=i: Turn(button[i], i))

    button[12].config(state="disable")
    button[13].config(state="disable")

    current_player = Player

    l.config(text=f"{current_player}'s Turn")


for i in ln:
    sl = Label(root, text=i, fg="white", bg="black", font=("Helvetica", 10, "bold"))
    label.append(sl)

for i in range(9):
    btn = Button(
        root,
        bg="black",
        width=2,
        font=("Helvetica", 30, "bold"),
        state="disable",
        bd=30,
    )
    button.append(btn)

bn = [("EXIT", "REMATCH", "RESTART"), (root.destroy, Rematch, Restart)]

for i in range(3):
    btn2 = Button(
        root,
        text=bn[0][i],
        bg="black",
        fg="white",
        font=("Helvetica", 5, "bold"),
        bd=15,
        command=bn[1][i],
        state="disable",
    )
    button.append(btn2)

button[9].config(state="normal")

for i in range(2):
    sl1 = Label(root, font=("Helvetica", 1, "bold"))
    btn3 = Button(
        root,
        text=p[i],
        bg="black",
        fg="white",
        font=("Helvetica", 9, "bold"),
        bd=15,
        command=lambda i=i: set_current_player(p[i]),
    )
    button.append(btn3)
    label.append(sl1)

l = Label(root, fg="white", bg="black", font=("Helvetica", 15, "bold"))


label[0].grid(column=1)
label[1].grid(column=1)
l.grid(column=1, pady=70)
label[2].grid(columnspan=2)
label[3].grid(row=3, column=1, columnspan=2)

for i in range(3):
    button[i].grid(row=4, column=i)
for i in range(3, 6):
    x += 1
    button[i].grid(row=5, column=x)
for i in range(6, 9):
    y += 1
    button[i].grid(row=6, column=y)


button[10].grid(row=8, ipadx=45, pady=50)
button[11].grid(row=8, column=2, ipadx=50)
button[12].grid(row=10, columnspan=2, ipadx=50)
button[13].grid(row=10, column=1, columnspan=2, ipadx=50)
button[9].grid(column=1, pady=50, ipadx=50)

root.mainloop()
