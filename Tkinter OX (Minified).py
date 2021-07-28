from tkinter import Tk,Label as Z,Button as a
import random as h
Y=''
X='O'
W='X'
V=None
T='bold'
S='Helvetica'
R='white'
L='black'
K='normal'
J='disable'
H=range
F=' '
I=Tk()
I.config(bg=L)
D=V
G=V
A=[F]*9
M=0
N=0
O=0
P=0
U=[W,X]
c=[f"TOTAL : {O}",f"TIE : {P}",f"X : {M}",f"O : {N}"]
C=[]
B=[]
d,e=-1,-1
def i():
	global G,D,A,M,N,O,P,U;I=h.choice(U);O+=1;D=I;C[0].config(text=f"TOTAL : {O}")
	if F not in A:P+=1;C[1].config(text=f"TIE : {P}")
	if G==W:M+=1;C[2].config(text=f"X : {M}")
	elif G==X:N+=1;C[3].config(text=f"O : {N}")
	for E in H(4,6):C[E].config(text=Y,bg=L,width=0,height=0);B[E+6].config(state=J)
	G=V;f(D)
	for E in H(9):B[E].config(text=Y);A[E]=F
def j():
	global G,D,A,M,N,O,P;O=0;P=0;M=0;N=0
	for E in H(4):C[E].config(text=c[E])
	for E in H(9):B[E].config(text=Y,state=J);A[E]=F
	for E in H(12,14):B[E].config(state=K);C[E-8].config(text=Y,bg=L,width=0,height=0);B[E-2].config(state=J)
	Q.config(text=Y);G=V;D=V
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
	if A:C[4].config(text='_',width=330,bg=R);G=A
	elif B:C[5].config(text='|',bg=R,width=3,height=116);G=B
	elif D:G=D
def b():pass
def o(Button,Position):
	E=Position;C=Button;global D
	if D==W:
		if A[E]==F:A[E]=D;C.config(command=b,state=J)
		C.config(text=D,fg='yellow',state=K);D=X
	elif D==X:
		if A[E]==F:A[E]=D;C.config(command=b,state=J)
		C.config(text=D,fg='orange',state=K);D=W
	Q.config(text=f"{D}'s Turn")
	if F not in A:Q.config(text="It's A Tie");B[10].config(state=K);B[11].config(state=K)
	n()
	if G==W or G==X:
		Q.config(text=f"{G} WON ");B[10].config(state=K);B[11].config(state=K)
		for I in H(9):B[I].config(command=b)
def f(Player):
	global D
	for A in H(9):B[A].config(state=K,command=lambda i=A:o(B[i],i))
	B[12].config(state=J);B[13].config(state=J);D=Player;Q.config(text=f"{D}'s Turn")
for E in c:p=Z(I,text=E,fg=R,bg=L,font=(S,10,T));C.append(p)
for E in H(9):q=a(I,bg=L,width=2,font=(S,30,T),state=J,bd=30);B.append(q)
g=[('EXIT','REMATCH','RESTART'),(I.destroy,i,j)]
for E in H(3):r=a(I,text=g[0][E],bg=L,fg=R,font=(S,5,T),bd=15,command=g[1][E],state=J);B.append(r)
B[9].config(state=K)
for E in H(2):s=Z(I,font=(S,1,T));t=a(I,text=U[E],bg=L,fg=R,font=(S,9,T),bd=15,command=lambda i=E:f(U[i]));B.append(t);C.append(s)
Q=Z(I,fg=R,bg=L,font=(S,15,T))
C[0].grid(column=1)
C[1].grid(column=1)
Q.grid(column=1,pady=70)
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
I.mainloop()
