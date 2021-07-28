from tkinter import Tk,Label as Z,Button as a
import random as h
Y='O'
X='X'
W=None
U='bold'
T='Helvetica'
S='white'
R=''
M='black'
L='normal'
I='disable'
H=range
F=' '
J=Tk()
J.config(bg=M)
D=W
G=W
A=[F]*9
N=0
O=0
P=0
Q=0
V=[X,Y]
c=[f"TOTAL : {P}",f"TIE : {Q}",f"X : {N}",f"O : {O}"]
C=[]
B=[]
d,e=-1,-1
def i():
	global G,D,A,N,O,P,Q,V;L=h.choice(V);P+=1;D=L;K.config(text=D)
	if F not in A:Q+=1;C[1].config(text=f"TIE : {Q}")
	if G==X:N+=1;C[2].config(text=f"X : {N}")
	elif G==Y:O+=1;C[3].config(text=f"O : {O}")
	for E in H(4,6):C[E].config(text=R,bg=M,width=0,height=0)
	K.config(text=R);C[0].config(text=f"TOTAL : {P}");G=W;f(D);J=-1
	for E in A:J+=1;A[J]=F
	for E in H(9):B[E].config(text=R)
	B[10].config(state=I);B[11].config(state=I)
def j():
	global G,D,A,N,O,P,Q;P=0;Q=0;N=0;O=0
	for E in H(4):C[E].config(text=c[E])
	for E in H(9):B[E].config(text=R,state=I)
	for E in H(12,14):B[E].config(state=L)
	for E in H(4,6):C[E].config(text=R,bg=M,width=0,height=0)
	K.config(text=R);G=W;D=W;J=-1
	for E in A:J+=1;A[J]=F
	B[10].config(state=I);B[11].config(state=I)
def k():
	B='s';D=A[0]==A[1]==A[2]!=F;E=A[3]==A[4]==A[5]!=F;G=A[6]==A[7]==A[8]!=F
	if D:C[4].grid(row=3,sticky=B,columnspan=3,rowspan=2,pady=140);return A[0]
	elif E:C[4].grid(row=3,sticky=B,columnspan=3,rowspan=3,pady=140);return A[3]
	elif G:C[4].grid(row=3,sticky=B,columnspan=3,rowspan=4,pady=140);return A[6]
def l():
	B='e';D=A[0]==A[3]==A[6]!=F;E=A[1]==A[4]==A[7]!=F;G=A[2]==A[5]==A[8]!=F
	if D:C[5].grid(row=4,sticky=B,rowspan=3,padx=170,columnspan=1);return A[0]
	elif E:C[5].grid(row=4,sticky=B,rowspan=3,padx=173,columnspan=2);return A[1]
	elif G:C[5].grid(row=4,sticky=B,rowspan=3,padx=173,columnspan=3);return A[2]
def m():
	B=A[0]==A[4]==A[8]!=F;C=A[2]==A[4]==A[6]!=F
	if B:return A[0]
	elif C:return A[2]
def n():
	global G;A=k();B=l();D=m()
	if A:C[4].config(text='_',width=330,bg=S);G=A
	elif B:C[5].config(text='|',bg=S,width=3,height=116);G=B
	elif D:G=D
def b():pass
def o(Button,Position):
	E=Position;C=Button;global D
	if D==X:
		if A[E]==F:A[E]=D;C.config(command=b,state=I)
		C.config(text=D,fg='yellow',state=L);D=Y
	elif D==Y:
		if A[E]==F:A[E]=D;C.config(command=b,state=I)
		C.config(text=D,fg='orange',state=L);D=X
	K.config(text=f"{D}'s Turn")
	if F not in A:K.config(text="It's A Tie");B[10].config(state=L);B[11].config(state=L)
	n()
	if G==X or G==Y:
		K.config(text=f"{G} WON ");B[10].config(state=L);B[11].config(state=L)
		for J in H(9):B[J].config(command=b)
def f(Player):
	global D
	for A in H(9):B[A].config(state=L,command=lambda i=A:o(B[i],i))
	B[12].config(state=I);B[13].config(state=I);D=Player;K.config(text=f"{D}'s Turn")
for E in c:p=Z(J,text=E,fg=S,bg=M,font=(T,10,U));C.append(p)
for E in H(9):q=a(J,bg=M,width=2,font=(T,30,U),state=I,bd=30);B.append(q)
g=[('EXIT','REMATCH','RESTART'),(J.destroy,i,j)]
for E in H(3):r=a(J,text=g[0][E],bg=M,fg=S,font=(T,5,U),bd=15,command=g[1][E],state=I);B.append(r)
B[9].config(state=L)
for E in H(2):s=Z(J,font=(T,1,U));t=a(J,text=V[E],bg=M,fg=S,font=(T,9,U),bd=15,command=lambda i=E:f(V[i]));B.append(t);C.append(s)
K=Z(J,fg=S,bg=M,font=(T,15,U))
C[0].grid(column=1)
C[1].grid(column=1)
K.grid(column=1,pady=70)
C[2].grid(columnspan=2)
C[3].grid(row=3,column=1,columnspan=2)
for E in H(3):B[E].grid(row=4,column=E)
for E in H(3,6):d+=1;B[E].grid(row=5,column=d)
for E in H(6,9):e+=1;B[E].grid(row=6,column=e)
B[10].grid(row=8,ipadx=45,pady=50)
B[11].grid(row=8,column=2,ipadx=50)
B[12].grid(row=10,columnspan=2,ipadx=50)
B[13].grid(row=10,column=1,columnspan=2,ipadx=50)
B[9].grid(column=1,pady=50,ipadx=50)
J.mainloop()
