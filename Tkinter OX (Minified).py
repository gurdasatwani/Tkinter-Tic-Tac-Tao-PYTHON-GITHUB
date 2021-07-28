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
C=' '
J=Tk()
J.config(bg=M)
E=W
G=W
A=[C,C,C,C,C,C,C,C,C]
N=0
O=0
P=0
Q=0
V=[X,Y]
c=[f"TOTAL : {P}",f"TIE : {Q}",f"X : {N}",f"O : {O}"]
D=[]
B=[]
d,e=-1,-1
def i():
	global G,E,A,N,O,P,Q,V;L=h.choice(V);P+=1;E=L;K.config(text=E)
	if C not in A:Q+=1;D[1].config(text=f"TIE : {Q}")
	if G==X:N+=1;D[2].config(text=f"X : {N}")
	elif G==Y:O+=1;D[3].config(text=f"O : {O}")
	for F in H(4,6):D[F].config(text=R,bg=M,width=0,height=0)
	K.config(text=R);D[0].config(text=f"TOTAL : {P}");G=W;f(E);J=-1
	for F in A:J+=1;A[J]=C
	for F in H(9):B[F].config(text=R)
	B[10].config(state=I);B[11].config(state=I)
def j():
	global G,E,A,N,O,P,Q;P=0;Q=0;N=0;O=0
	for F in H(4):D[F].config(text=c[F])
	for F in H(9):B[F].config(text=R,state=I)
	for F in H(12,14):B[F].config(state=L)
	for F in H(4,6):D[F].config(text=R,bg=M,width=0,height=0)
	K.config(text=R);G=W;E=W;J=-1
	for F in A:J+=1;A[J]=C
	B[10].config(state=I);B[11].config(state=I)
def k():
	B='s';E=A[0]==A[1]==A[2]!=C;F=A[3]==A[4]==A[5]!=C;G=A[6]==A[7]==A[8]!=C
	if E:D[4].grid(row=3,sticky=B,columnspan=3,rowspan=2,pady=140);return A[0]
	elif F:D[4].grid(row=3,sticky=B,columnspan=3,rowspan=3,pady=140);return A[3]
	elif G:D[4].grid(row=3,sticky=B,columnspan=3,rowspan=4,pady=140);return A[6]
def l():
	B='e';E=A[0]==A[3]==A[6]!=C;F=A[1]==A[4]==A[7]!=C;G=A[2]==A[5]==A[8]!=C
	if E:D[5].grid(row=4,sticky=B,rowspan=3,padx=170,columnspan=1);return A[0]
	elif F:D[5].grid(row=4,sticky=B,rowspan=3,padx=173,columnspan=2);return A[1]
	elif G:D[5].grid(row=4,sticky=B,rowspan=3,padx=173,columnspan=3);return A[2]
def m():
	B=A[0]==A[4]==A[8]!=C;D=A[2]==A[4]==A[6]!=C
	if B:return A[0]
	elif D:return A[2]
def n():
	global G;A=k();B=l();C=m()
	if A:D[4].config(text='_',width=330,bg=S);G=A
	elif B:D[5].config(text='|',bg=S,width=3,height=116);G=B
	elif C:G=C
def b():pass
def o(Button,Position):
	F=Position;D=Button;global E
	if E==X:
		if A[F]==C:A[F]=E;D.config(command=b,state=I)
		D.config(text=E,fg='yellow',state=L);E=Y
	elif E==Y:
		if A[F]==C:A[F]=E;D.config(command=b,state=I)
		D.config(text=E,fg='orange',state=L);E=X
	K.config(text=f"{E}'s Turn")
	if C not in A:K.config(text="It's A Tie");B[10].config(state=L);B[11].config(state=L)
	n()
	if G==X or G==Y:
		K.config(text=f"{G} WON ");B[10].config(state=L);B[11].config(state=L)
		for J in H(9):B[J].config(command=b)
def f(Player):
	global E
	for A in H(9):B[A].config(state=L,command=lambda i=A:o(B[i],i))
	B[12].config(state=I);B[13].config(state=I);E=Player;K.config(text=f"{E}'s Turn")
for F in c:p=Z(J,text=F,fg=S,bg=M,font=(T,10,U));D.append(p)
for F in H(9):q=a(J,bg=M,width=2,font=(T,30,U),state=I,bd=30);B.append(q)
g=[('EXIT','REMATCH','RESTART'),(J.destroy,i,j)]
for F in H(3):r=a(J,text=g[0][F],bg=M,fg=S,font=(T,5,U),bd=15,command=g[1][F],state=I);B.append(r)
B[9].config(state=L)
for F in H(2):s=Z(J,font=(T,1,U));t=a(J,text=V[F],bg=M,fg=S,font=(T,9,U),bd=15,command=lambda i=F:f(V[i]));B.append(t);D.append(s)
K=Z(J,fg=S,bg=M,font=(T,15,U))
D[0].grid(column=1)
D[1].grid(column=1)
K.grid(column=1,pady=70)
D[2].grid(columnspan=2)
D[3].grid(row=3,column=1,columnspan=2)
for F in H(3):B[F].grid(row=4,column=F)
for F in H(3,6):d+=1;B[F].grid(row=5,column=d)
for F in H(6,9):e+=1;B[F].grid(row=6,column=e)
B[10].grid(row=8,ipadx=45,pady=50)
B[11].grid(row=8,column=2,ipadx=50)
B[12].grid(row=10,columnspan=2,ipadx=50)
B[13].grid(row=10,column=1,columnspan=2,ipadx=50)
B[9].grid(column=1,pady=50,ipadx=50)
J.mainloop()
