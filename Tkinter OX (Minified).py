from tkinter import Tk,Label as O,Button as I
import random as u
k=None
X='O'
W='X'
T=''
N='normal'
K='white'
H='disable'
F='bold'
E='Helvetica'
D=' '
C='black'
B=Tk()
B.config(bg=C)
G=k
J=k
A=[D,D,D,D,D,D,D,D,D]
P=0
Q=0
R=0
S=0
t=[W,X]
def v():
	global J,G,A,P,Q,R,S,t;F=u.choice(t);R+=1;G=F;M.config(text=G)
	if D not in A:S+=1;s.config(text=f"TIE : {S}")
	if J==W:P+=1;p.config(text=f"X : {P}")
	elif J==X:Q+=1;q.config(text=f"O : {Q}")
	M.config(text=T),U.config(text=T,width=0,bg=C),V.config(text=T,bg=C,width=0,height=0),r.config(text=f"TOTAL : {R}");J=k;m(G);B=-1
	for E in A:B+=1;A[B]=D
	for E in Z:E.config(text=T)
	Y.config(state=H);a.config(state=H)
def w():
	global J,G,A,P,Q,R,S;R=0;S=0;s.config(text=f"TIE : {S}");P=0;p.config(text=f"X : {P}");Q=0;q.config(text=f"O : {Q}")
	for B in Z:B.config(state=H)
	n.config(state=N),o.config(state=N),M.config(text=T),U.config(text=T,width=0,bg=C),V.config(text=T,bg=C,width=0,height=0),r.config(text=f"TOTAL : {R}");J=k;G=k;E=-1
	for B in A:E+=1;A[E]=D
	for B in Z:B.config(text=T)
	a.config(state=H);Y.config(state=H)
def l():pass
def x():
	B='s';C=A[0]==A[1]==A[2]!=D;E=A[3]==A[4]==A[5]!=D;F=A[6]==A[7]==A[8]!=D
	if C:U.grid(row=3,sticky=B,columnspan=3,rowspan=2,pady=140);return A[0]
	elif E:U.grid(row=3,sticky=B,columnspan=3,rowspan=3,pady=140);return A[3]
	elif F:U.grid(row=3,sticky=B,columnspan=3,rowspan=4,pady=140);return A[6]
def y():
	B='e';C=A[0]==A[3]==A[6]!=D;E=A[1]==A[4]==A[7]!=D;F=A[2]==A[5]==A[8]!=D
	if C:V.grid(row=4,sticky=B,rowspan=3,padx=170,columnspan=1);return A[0]
	elif E:V.grid(row=4,sticky=B,rowspan=3,padx=173,columnspan=2);return A[1]
	elif F:V.grid(row=4,sticky=B,rowspan=3,padx=173,columnspan=3);return A[2]
def z():
	B=A[0]==A[4]==A[8]!=D;C=A[2]==A[4]==A[6]!=D
	if B:return A[0]
	elif C:return A[2]
def A0():
	global J;A=x();B=y();C=z()
	if A:U.config(text='_',width=330,bg=K);J=A
	elif B:V.config(text='|',bg=K,width=3,height=116);J=B
	elif C:J=C
def L(Button,Position):
	C=Position;B=Button;global G
	if G==W:
		if A[C]==D:A[C]=G;B.config(command=l,state=H)
		B.config(text=G,fg='yellow',state=N);G=X
	elif G==X:
		if A[C]==D:A[C]=G;B.config(command=l,state=H)
		B.config(text=G,fg='orange',state=N);G=W
	M.config(text=f"{G}'s Turn")
	if D not in A:M.config(text="It's A Tie");a.config(state=N);Y.config(state=N)
	A0()
	if J==W or J==X:
		M.config(text=f"{J} WON ");a.config(state=N);Y.config(state=N)
		for E in Z:E.config(command=l)
def m(Player):
	global G
	for A in Z:A.config(state=N)
	n.config(state=H),o.config(state=H);G=Player;M.config(text=f"{G}'s Turn");b.config(command=lambda:L(b,0)),c.config(command=lambda:L(c,1)),d.config(command=lambda:L(d,2)),e.config(command=lambda:L(e,3)),f.config(command=lambda:L(f,4)),g.config(command=lambda:L(g,5)),h.config(command=lambda:L(h,6)),i.config(command=lambda:L(i,7)),j.config(command=lambda:L(j,8))
n=I(B,text=X,bg=C,fg=K,font=(E,9,F),bd=15,command=lambda:m(X))
o=I(B,text=W,bg=C,fg=K,font=(E,9,F),bd=15,command=lambda:m(W))
A1=I(B,text='EXIT',bg=C,fg=K,font=(E,5,F),bd=15,command=B.destroy)
Y=I(B,text='REMATCH',bg=C,fg=K,font=(E,5,F),bd=15,command=v,state=H)
a=I(B,text='RESTART',bg=C,fg=K,font=(E,5,F),bd=15,command=w,state=H)
b=I(B,bg=C,width=2,font=(E,30,F),state=H,bd=30)
c=I(B,bg=C,width=2,font=(E,30,F),state=H,bd=30)
d=I(B,bg=C,width=2,font=(E,30,F),state=H,bd=30)
e=I(B,bg=C,width=2,font=(E,30,F),state=H,bd=30)
f=I(B,bg=C,width=2,font=(E,30,F),state=H,bd=30)
g=I(B,bg=C,width=2,font=(E,30,F),state=H,bd=30)
h=I(B,bg=C,width=2,font=(E,30,F),state=H,bd=30)
i=I(B,bg=C,width=2,font=(E,30,F),state=H,bd=30)
j=I(B,bg=C,width=2,font=(E,30,F),state=H,bd=30)
Z=[b,c,d,e,f,g,h,i,j]
M=O(B,fg=K,bg=C,font=(E,15,F))
U=O(B,font=(E,1,F))
V=O(B,font=(E,1,F))
p=O(B,text=f"X : {P}",fg=K,bg=C,font=(E,10,F))
q=O(B,text=f"O : {Q}",fg=K,bg=C,font=(E,10,F))
r=O(B,text=f"TOTAL : {R}",fg=K,bg=C,font=(E,10,F))
s=O(B,text=f"TIE : {S}",fg=K,bg=C,font=(E,10,F))
r.grid(column=1)
s.grid(column=1)
M.grid(column=1,pady=70)
p.grid(columnspan=2)
q.grid(row=3,column=1,columnspan=2)
b.grid(row=4)
c.grid(row=4,column=1)
d.grid(row=4,column=2)
e.grid(row=5)
f.grid(row=5,column=1)
g.grid(row=5,column=2)
h.grid(row=6)
i.grid(row=6,column=1)
j.grid(row=6,column=2)
Y.grid(row=8,ipadx=50,pady=50)
a.grid(row=8,column=2,ipadx=50)
o.grid(row=10,columnspan=2,ipadx=50)
n.grid(row=10,column=1,columnspan=2,ipadx=50)
A1.grid(column=1,pady=50,ipadx=50)
B.mainloop()
