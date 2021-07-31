from tkinter import Tk, Label, Button
import random

root = Tk()
root.config(bg="black")

current_player = None

winner = None

values = [" "] * 9

Xscore = 0

Oscore = 0

Total = 0

Tie = 0

p = ["X", "O"]

ln = [f"TOTAL : {Total}", f"TIE : {Tie}", f"X : {Xscore}", f"O : {Oscore}"]

label = []

button = []

x, y = -1, -1

def cnf(item,s,e,state=None,text=None,co=None,bg=None,width=None,height=None,font=None):
	
	for i in range(s,e):
		item[i].config(state=state,text=text,command=co,bg=bg,width=width,height=height,font=font)

def Rematch():

    global winner, current_player, values, Xscore, Oscore, Total, Tie, p

    Rp = random.choice(p)

    Total += 1

    current_player = Rp

    if " " not in values:

        Tie += 1

    if winner == "X":

        Xscore += 1

    elif winner == "O":

        Oscore += 1

    for i,x in zip(range(4),[f"TOTAL : {Total}",f"TIE : {Tie}",f"X : {Xscore}",f"O : {Oscore}"]):
 
     	label[i].config(text=x)

    cnf(label,4,6,text='',bg='black',width=0,height=0)

    cnf(button,10,12,state='disable')

    winner = None

    set_current_player(current_player)

    cnf(button,0,9,text="")

    for i in range(9):

        values[i] = " "

def Restart():

    global winner, current_player, values, Xscore, Oscore, Total, Tie

    Total = 0

    Tie = 0

    Xscore = 0

    Oscore = 0

    for i in range(4):

        label[i].config(text=ln[i])

    for i in range(9):

    	values[i] = " "

    cnf(label,4,6,text='',bg='black',width=0,height=0)

    cnf(button,0,9,state='disable',text="")
    cnf(button,12,14,state='normal')
    cnf(button,10,12,state='disable')

    l.config(text="")

    winner = None

    current_player = None

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

        cnf(button,10,12,state='normal')

    check_for_winner()

    if winner == "X" or winner == "O":

        l.config(text=f"{winner} WON ")

        cnf(button,10,12,state='normal')

        cnf(button,0,9,co=passs)

def set_current_player(Player):

    global current_player

    for i in range(9):

        button[i].config(command=lambda i=i: Turn(button[i], i))
 
    cnf(button,0,9,state='normal')
    cnf(button,12,14,state='disable')

    current_player = Player

    l.config(text=f"{current_player}'s Turn")

for i in ln:
    sl = Label(root, text=i, fg="white", bg="black", font=("Helvetica", 10, "bold"))
    label.append(sl)

bn = [(9,10,11,12,13),(root.destroy,Rematch, Restart,lambda:set_current_player(p[0]),lambda:set_current_player(p[1]))]

for m,k,z,o in zip([['']*9,['EXIT','REMATCH','RESTART',p[0],p[1]]],
[[2]*9,[0]*5],
[[30]*9,[5]*5],
[[30]*9,[15]*5]):
	for t,w,f,b in zip(m,k,z,o):
	       btn = Button(root,text=t,bg="black",fg='white',width=w,font=("Helvetica", f, "bold"),state="disable",bd=b)
	       button.append(btn)

for i in range(5):
	button[bn[0][i]].config(state='normal',command=bn[1][i])

cnf(button,10,12,state='disable')
cnf(button,12,14,font=("Helvetica",9, "bold"))
for i in range(2):
    sl1 = Label(root, font=("Helvetica", 1, "bold"))
    label.append(sl1)

l = Label(root, fg="white", bg="black", font=("Helvetica", 15, "bold"))


for (r,c,cs) in zip([0,1,3,3],[1,1,0,1],[1,1,2,2]):
	y+=1
	label[y].grid(row=r, column=c, columnspan=cs)
l.grid(row=2,column=1, pady=70)

for i in [[4]*3,[5]*3,[6]*3]:
	for r,c in zip(i,[0,1,2]*3):
	   x += 1
	   button[x].grid(row=r, column=c)

for (n,r,c,cs,ip) in zip([10,11,12,13,9],[8,8,10,10,11],[0,2,0,1,1],[1,1,2,2,1],[45,50,50,50,50]):
	button[n].grid(row=r,column=c,columnspan=cs, ipadx=ip, pady=50)
root.mainloop()
