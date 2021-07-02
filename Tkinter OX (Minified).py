q='|'
p='_'
o=None
e='normal'
Y='O'
X='X'
J='disable'
I='white'
G='black'
E='bold'
D='Helvetica'
C=' '
from tkinter import Tk,Label as M,Button as H
B=Tk()
B.config(bg=G)
F=o
L=o
A=[C,C,C,C,C,C,C,C,C]
def Z():pass
def f():
	B=A[0]==A[1]==A[2]!=C;D=A[3]==A[4]==A[5]!=C;E=A[6]==A[7]==A[8]!=C
	if B:return A[0]
	elif D:return A[3]
	elif E:return A[6]
def g():
	B=A[0]==A[3]==A[6]!=C;D=A[1]==A[4]==A[7]!=C;E=A[2]==A[5]==A[8]!=C
	if B:return A[0]
	elif D:return A[1]
	elif E:return A[2]
def h():
	B=A[0]==A[4]==A[8]!=C;D=A[2]==A[4]==A[6]!=C
	if B:return A[0]
	elif D:return A[2]
def i():
	global L;A=f();B=g();C=h()
	if A:L=A
	elif B:L=B
	elif C:L=C
def K(Button,Position):
	D=Position;B=Button;global F
	if F==X:
		if A[D]==C:A[D]=F;B.config(command=Z,state=J)
		B.config(text=F,fg='yellow',state=e);F=Y
	elif F==Y:
		if A[D]==C:A[D]=F;B.config(command=Z,state=J)
		B.config(text=F,fg='orange',state=e);F=X
	N.config(text=f"{F}'s Turn")
	if C not in A:N.config(text="It's A Tie")
	i()
	if L==X or L==Y:
		N.config(text=f"{L} WON ")
		for E in d:E.config(command=Z)
def a(Player):
	global F
	for A in d:A.config(state=e)
	b.destroy(),c.destroy();F=Player;N.config(text=f"{F}'s Turn");O.config(command=lambda:K(O,0)),P.config(command=lambda:K(P,1)),Q.config(command=lambda:K(Q,2)),R.config(command=lambda:K(R,3)),S.config(command=lambda:K(S,4)),T.config(command=lambda:K(T,5)),U.config(command=lambda:K(U,6)),V.config(command=lambda:K(V,7)),W.config(command=lambda:K(W,8))
b=H(B,text=Y,bg=G,fg=I,font=(D,9,E),bd=10,command=lambda:a(Y))
c=H(B,text=X,bg=G,fg=I,font=(D,9,E),bd=10,command=lambda:a(X))
j=H(B,text='EXIT',bg=G,fg=I,font=(D,5,E),bd=10,command=B.destroy)
O=H(B,bg=G,width=2,font=(D,40,E),state=J)
P=H(B,bg=G,width=2,font=(D,40,E),state=J)
Q=H(B,bg=G,width=2,font=(D,40,E),state=J)
R=H(B,bg=G,width=2,font=(D,40,E),state=J)
S=H(B,bg=G,width=2,font=(D,40,E),state=J)
T=H(B,bg=G,width=2,font=(D,40,E),state=J)
U=H(B,bg=G,width=2,font=(D,40,E),state=J)
V=H(B,bg=G,width=2,font=(D,40,E),state=J)
W=H(B,bg=G,width=2,font=(D,40,E),state=J)
k=M(B,text=p,fg=I,bg=I,font=(D,1,E),width=355)
l=M(B,text=p,fg=I,bg=I,font=(D,1,E),width=355)
m=M(B,text=q,fg=I,bg=I,font=(D,1,E),height=134)
n=M(B,text=q,fg=I,bg=I,font=(D,1,E),height=134)
N=M(B,fg=I,bg=G,font=(D,15,E))
d=[O,P,Q,R,S,T,U,V,W]
b.place(x=645,y=1640)
c.place(x=278,y=1640)
j.place(x=450,y=1500)
O.place(y=490)
P.place(x=360,y=490)
Q.place(x=710,y=490)
R.place(y=810)
S.place(x=360,y=810)
T.place(x=710,y=810)
U.place(y=1130)
V.place(x=360,y=1130)
W.place(x=710,y=1130)
m.place(x=355,y=490)
n.place(x=710,y=490)
k.place(y=795)
l.place(y=1115)
N.place(x=370,y=200)
B.mainloop()