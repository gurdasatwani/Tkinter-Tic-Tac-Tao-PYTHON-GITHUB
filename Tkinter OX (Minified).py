s='|'
r='_'
f=None
b='O'
a='X'
N='normal'
J='white'
H='disable'
G='black'
E='bold'
D='Helvetica'
C=' '
from tkinter import Tk,Label as O,Button as I
B=Tk()
B.config(bg=G)
F=f
K=f
A=[C,C,C,C,C,C,C,C,C]
def h():
	global K,F,A
	for B in Z:B.config(state=H)
	d.config(state=N),e.config(state=N);M.config(text='');K=f;F=f;D=-1
	for B in A:D+=1;A[D]=C
	for B in Z:B.config(text='')
	P.config(state=H)
def c():0
def i():
	B=A[0]==A[1]==A[2]!=C;D=A[3]==A[4]==A[5]!=C;E=A[6]==A[7]==A[8]!=C
	if B:return A[0]
	elif D:return A[3]
	elif E:return A[6]
def j():
	B=A[0]==A[3]==A[6]!=C;D=A[1]==A[4]==A[7]!=C;E=A[2]==A[5]==A[8]!=C
	if B:return A[0]
	elif D:return A[1]
	elif E:return A[2]
def k():
	B=A[0]==A[4]==A[8]!=C;D=A[2]==A[4]==A[6]!=C
	if B:return A[0]
	elif D:return A[2]
def l():
	global K;A=i();B=j();C=k()
	if A:K=A
	elif B:K=B
	elif C:K=C
def L(Button,Position):
	D=Position;B=Button;global F
	if F==a:
		if A[D]==C:A[D]=F;B.config(command=c,state=H)
		B.config(text=F,fg='yellow',state=N);F=b
	elif F==b:
		if A[D]==C:A[D]=F;B.config(command=c,state=H)
		B.config(text=F,fg='orange',state=N);F=a
	M.config(text=f"{F}'s Turn")
	if C not in A:M.config(text="It's A Tie");P.config(state=N);P.place(x=420,y=1800)
	l()
	if K==a or K==b:
		M.config(text=f"{K} WON ");P.config(state=N)
		for E in Z:E.config(command=c)
		P.place(x=420,y=1800)
def g(Player):
	global F
	for A in Z:A.config(state=N)
	d.config(state=H),e.config(state=H);F=Player;M.config(text=f"{F}'s Turn");Q.config(command=lambda:L(Q,0)),R.config(command=lambda:L(R,1)),S.config(command=lambda:L(S,2)),T.config(command=lambda:L(T,3)),U.config(command=lambda:L(U,4)),V.config(command=lambda:L(V,5)),W.config(command=lambda:L(W,6)),X.config(command=lambda:L(X,7)),Y.config(command=lambda:L(Y,8))
d=I(B,text=b,bg=G,fg=J,font=(D,9,E),bd=10,command=lambda:g(b))
e=I(B,text=a,bg=G,fg=J,font=(D,9,E),bd=10,command=lambda:g(a))
m=I(B,text='EXIT',bg=G,fg=J,font=(D,5,E),bd=10,command=B.destroy)
P=I(B,text='RESTART',bg=G,fg=J,font=(D,5,E),bd=10,command=h)
Q=I(B,bg=G,width=2,font=(D,40,E),state=H)
R=I(B,bg=G,width=2,font=(D,40,E),state=H)
S=I(B,bg=G,width=2,font=(D,40,E),state=H)
T=I(B,bg=G,width=2,font=(D,40,E),state=H)
U=I(B,bg=G,width=2,font=(D,40,E),state=H)
V=I(B,bg=G,width=2,font=(D,40,E),state=H)
W=I(B,bg=G,width=2,font=(D,40,E),state=H)
X=I(B,bg=G,width=2,font=(D,40,E),state=H)
Y=I(B,bg=G,width=2,font=(D,40,E),state=H)
n=O(B,text=r,fg=J,bg=J,font=(D,1,E),width=355)
o=O(B,text=r,fg=J,bg=J,font=(D,1,E),width=355)
p=O(B,text=s,fg=J,bg=J,font=(D,1,E),height=134)
q=O(B,text=s,fg=J,bg=J,font=(D,1,E),height=134)
M=O(B,fg=J,bg=G,font=(D,15,E))
Z=[Q,R,S,T,U,V,W,X,Y]
d.place(x=645,y=1640)
e.place(x=278,y=1640)
m.place(x=450,y=1500)
Q.place(y=490)
R.place(x=360,y=490)
S.place(x=710,y=490)
T.place(y=810)
U.place(x=360,y=810)
V.place(x=710,y=810)
W.place(y=1130)
X.place(x=360,y=1130)
Y.place(x=710,y=1130)
p.place(x=355,y=490)
q.place(x=710,y=490)
n.place(y=795)
o.place(y=1115)
M.place(x=370,y=200)
B.mainloop()
