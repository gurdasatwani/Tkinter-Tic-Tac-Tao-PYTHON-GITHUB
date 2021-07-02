from tkinter import Tk,Label as M,Button as J
k='|'
j='_'
h=None
d='O'
c='X'
O='normal'
I='white'
H='disable'
F='black'
E='bold'
D='Helvetica'
C=' '
B=Tk()
B.config(bg=F)
G=h
K=h
A=[C,C,C,C,C,C,C,C,C]
def l():
	D='';global K,G,A
	for B in b:B.config(state=H)
	f.config(state=O),g.config(state=O);N.config(text=D),Q.config(text=D,width=0,bg=F),R.config(text=D,bg=F,width=0,height=0);K=h;G=h;E=-1
	for B in A:E+=1;A[E]=C
	for B in b:B.config(text=D)
	P.config(state=H)
def e():pass
def m():
	B=A[0]==A[1]==A[2]!=C;D=A[3]==A[4]==A[5]!=C;E=A[6]==A[7]==A[8]!=C
	if B:Q.place(x=50,y=630);return A[0]
	elif D:Q.place(x=50,y=950);return A[3]
	elif E:Q.place(x=50,y=1270);return A[6]
	return
def n():
	B=A[0]==A[3]==A[6]!=C;D=A[1]==A[4]==A[7]!=C;E=A[2]==A[5]==A[8]!=C
	if B:R.place(x=175,y=535);return A[0]
	elif D:R.place(x=535,y=535);return A[1]
	elif E:R.place(x=885,y=535);return A[2]
def o():
	B=A[0]==A[4]==A[8]!=C;D=A[2]==A[4]==A[6]!=C
	if B:return A[0]
	elif D:return A[2]
def p():
	global K;A=m();B=n();C=o()
	if A:Q.config(text=j,width=320,bg=I);K=A
	elif B:R.config(text=k,bg=I,width=3,height=120);K=B
	elif C:K=C
def L(Button,Position):
	D=Position;B=Button;global G
	if G==c:
		if A[D]==C:A[D]=G;B.config(command=e,state=H)
		B.config(text=G,fg='yellow',state=O);G=d
	elif G==d:
		if A[D]==C:A[D]=G;B.config(command=e,state=H)
		B.config(text=G,fg='orange',state=O);G=c
	N.config(text=f"{G}'s Turn")
	if C not in A:N.config(text="It's A Tie");P.config(state=O);P.place(x=420,y=1800)
	p()
	if K==c or K==d:
		N.config(text=f"{K} WON ");P.config(state=O)
		for E in b:E.config(command=e)
		P.place(x=420,y=1800)
def i(Player):
	global G
	for A in b:A.config(state=O)
	f.config(state=H),g.config(state=H);G=Player;N.config(text=f"{G}'s Turn");S.config(command=lambda:L(S,0)),T.config(command=lambda:L(T,1)),U.config(command=lambda:L(U,2)),V.config(command=lambda:L(V,3)),W.config(command=lambda:L(W,4)),X.config(command=lambda:L(X,5)),Y.config(command=lambda:L(Y,6)),Z.config(command=lambda:L(Z,7)),a.config(command=lambda:L(a,8))
f=J(B,text=d,bg=F,fg=I,font=(D,9,E),bd=10,command=lambda:i(d))
g=J(B,text=c,bg=F,fg=I,font=(D,9,E),bd=10,command=lambda:i(c))
q=J(B,text='EXIT',bg=F,fg=I,font=(D,5,E),bd=10,command=B.destroy)
P=J(B,text='RESTART',bg=F,fg=I,font=(D,5,E),bd=10,command=l)
S=J(B,bg=F,width=2,font=(D,40,E),state=H)
T=J(B,bg=F,width=2,font=(D,40,E),state=H)
U=J(B,bg=F,width=2,font=(D,40,E),state=H)
V=J(B,bg=F,width=2,font=(D,40,E),state=H)
W=J(B,bg=F,width=2,font=(D,40,E),state=H)
X=J(B,bg=F,width=2,font=(D,40,E),state=H)
Y=J(B,bg=F,width=2,font=(D,40,E),state=H)
Z=J(B,bg=F,width=2,font=(D,40,E),state=H)
a=J(B,bg=F,width=2,font=(D,40,E),state=H)
r=M(B,text=j,fg=I,bg=I,font=(D,1,E),width=355)
s=M(B,text=j,fg=I,bg=I,font=(D,1,E),width=355)
t=M(B,text=k,fg=I,bg=I,font=(D,1,E),height=134)
u=M(B,text=k,fg=I,bg=I,font=(D,1,E),height=134)
N=M(B,fg=I,bg=F,font=(D,15,E))
Q=M(B,font=(D,1,E))
R=M(B,font=(D,1,E))
b=[S,T,U,V,W,X,Y,Z,a]
f.place(x=645,y=1640)
g.place(x=278,y=1640)
q.place(x=450,y=1500)
S.place(y=490)
T.place(x=360,y=490)
U.place(x=710,y=490)
V.place(y=810)
W.place(x=360,y=810)
X.place(x=710,y=810)
Y.place(y=1130)
Z.place(x=360,y=1130)
a.place(x=710,y=1130)
t.place(x=355,y=490)
u.place(x=710,y=490)
r.place(y=795)
s.place(y=1115)
N.place(x=370,y=200)
B.mainloop()
