s='|'
r='_'
l=None
T='O'
S='X'
O='normal'
I='disable'
G='white'
F='black'
E=' '
D='bold'
C='Helvetica'
from tkinter import Tk,Label as K,Button as J
B=Tk()
B.config(bg=F)
H=l
L=l
A=[E,E,E,E,E,E,E,E,E]
U=0
V=0
W=0
X=0
def t():
	C='';global L,H,A,U,V,W,X;W+=1
	if E not in A:X+=1;q.config(text=f"TIE : {X}")
	if L==S:U+=1;n.config(text=f"X : {U}")
	elif L==T:V+=1;o.config(text=f"O : {V}")
	for B in h:B.config(state=I)
	j.config(state=O),k.config(state=O),N.config(text=C),Q.config(text=C,width=0,bg=F),R.config(text=C,bg=F,width=0,height=0),p.config(text=f"TOTAL : {W}");L=l;H=l;D=-1
	for B in A:D+=1;A[D]=E
	for B in h:B.config(text=C)
	P.config(state=I)
def i():pass
def u():
	B=A[0]==A[1]==A[2]!=E;C=A[3]==A[4]==A[5]!=E;D=A[6]==A[7]==A[8]!=E
	if B:Q.place(x=50,y=630);return A[0]
	elif C:Q.place(x=50,y=950);return A[3]
	elif D:Q.place(x=50,y=1270);return A[6]
def v():
	B=A[0]==A[3]==A[6]!=E;C=A[1]==A[4]==A[7]!=E;D=A[2]==A[5]==A[8]!=E
	if B:R.place(x=175,y=535);return A[0]
	elif C:R.place(x=535,y=535);return A[1]
	elif D:R.place(x=885,y=535);return A[2]
def w():
	B=A[0]==A[4]==A[8]!=E;C=A[2]==A[4]==A[6]!=E
	if B:return A[0]
	elif C:return A[2]
def x():
	global L;A=u();B=v();C=w()
	if A:Q.config(text=r,width=320,bg=G);L=A
	elif B:R.config(text=s,bg=G,width=3,height=120);L=B
	elif C:L=C
def M(Button,Position):
	C=Position;B=Button;global H
	if H==S:
		if A[C]==E:A[C]=H;B.config(command=i,state=I)
		B.config(text=H,fg='yellow',state=O);H=T
	elif H==T:
		if A[C]==E:A[C]=H;B.config(command=i,state=I)
		B.config(text=H,fg='orange',state=O);H=S
	N.config(text=f"{H}'s Turn")
	if E not in A:N.config(text="It's A Tie");P.config(state=O);P.place(x=415,y=1500)
	x()
	if L==S or L==T:
		N.config(text=f"{L} WON ");P.config(state=O)
		for D in h:D.config(command=i)
		P.place(x=415,y=1500)
def m(Player):
	global H
	for A in h:A.config(state=O)
	j.config(state=I),k.config(state=I);H=Player;N.config(text=f"{H}'s Turn");Y.config(command=lambda:M(Y,0)),Z.config(command=lambda:M(Z,1)),a.config(command=lambda:M(a,2)),b.config(command=lambda:M(b,3)),c.config(command=lambda:M(c,4)),d.config(command=lambda:M(d,5)),e.config(command=lambda:M(e,6)),f.config(command=lambda:M(f,7)),g.config(command=lambda:M(g,8))
j=J(B,text=T,bg=F,fg=G,font=(C,9,D),bd=10,command=lambda:m(T))
k=J(B,text=S,bg=F,fg=G,font=(C,9,D),bd=10,command=lambda:m(S))
y=J(B,text='EXIT',bg=F,fg=G,font=(C,5,D),bd=10,command=B.destroy)
P=J(B,text='RESTART',bg=F,fg=G,font=(C,5,D),bd=10,command=t)
Y=J(B,bg=F,width=2,font=(C,40,D),state=I)
Z=J(B,bg=F,width=2,font=(C,40,D),state=I)
a=J(B,bg=F,width=2,font=(C,40,D),state=I)
b=J(B,bg=F,width=2,font=(C,40,D),state=I)
c=J(B,bg=F,width=2,font=(C,40,D),state=I)
d=J(B,bg=F,width=2,font=(C,40,D),state=I)
e=J(B,bg=F,width=2,font=(C,40,D),state=I)
f=J(B,bg=F,width=2,font=(C,40,D),state=I)
g=J(B,bg=F,width=2,font=(C,40,D),state=I)
z=K(B,text=s,fg=G,bg=G,font=(C,1,D),height=134)
A0=K(B,text=s,fg=G,bg=G,font=(C,1,D),height=134)
A1=K(B,text=r,fg=G,bg=G,font=(C,1,D),width=355)
A2=K(B,text=r,fg=G,bg=G,font=(C,1,D),width=355)
N=K(B,fg=G,bg=F,font=(C,15,D))
Q=K(B,font=(C,1,D))
R=K(B,font=(C,1,D))
n=K(B,text=f"X : {U}",fg=G,bg=F,font=(C,10,D))
o=K(B,text=f"O : {V}",fg=G,bg=F,font=(C,10,D))
p=K(B,text=f"TOTAL : {W}",fg=G,bg=F,font=(C,10,D))
q=K(B,text=f"TIE : {X}",fg=G,bg=F,font=(C,10,D))
h=[Y,Z,a,b,c,d,e,f,g]
j.place(x=645,y=1640)
k.place(x=278,y=1640)
y.place(x=445,y=1800)
Y.place(y=490)
Z.place(x=360,y=490)
a.place(x=710,y=490)
b.place(y=810)
c.place(x=360,y=810)
d.place(x=710,y=810)
e.place(y=1130)
f.place(x=360,y=1130)
g.place(x=710,y=1130)
z.place(x=355,y=490)
A0.place(x=710,y=490)
A1.place(y=795)
A2.place(y=1115)
N.place(x=370,y=200)
n.place(x=300,y=350)
o.place(x=650,y=350)
p.pack()
q.pack()
B.mainloop()
