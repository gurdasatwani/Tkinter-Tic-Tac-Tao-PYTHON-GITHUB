from tkinter import Tk,Label as d,Button as l
import random as m
c='bold'
b='Helvetica'
a='white'
Z='O'
Y='X'
X=''
W='black'
V=zip
S='normal'
L='disable'
K=range
H=None
F=' '
I=Tk()
I.config(bg=W)
B=H
G=H
A=[F]*9
M=0
N=0
O=0
P=0
Q=[Y,Z]
h=[f"TOTAL : {O}",f"TIE : {P}",f"X : {M}",f"O : {N}"]
D=[]
C=[]
i,j=-1,-1
def E(item,s,e,state=H,text=H,co=H,bg=H,width=H,height=H,font=H):
	for A in K(s,e):item[A].config(state=state,text=text,command=co,bg=bg,width=width,height=height,font=font)
def n():
	global G,B,A,M,N,O,P,Q;J=m.choice(Q);O+=1;B=J
	if F not in A:P+=1
	if G==Y:M+=1
	elif G==Z:N+=1
	for (I,R) in V(K(4),[f"TOTAL : {O}",f"TIE : {P}",f"X : {M}",f"O : {N}"]):D[I].config(text=R)
	E(D,4,6,text=X,bg=W,width=0,height=0);E(C,10,12,state=L);G=H;f(B);E(C,0,9,text=X)
	for I in K(9):A[I]=F
def o():
	global G,B,A,M,N,O,P;O=0;P=0;M=0;N=0
	for I in K(4):D[I].config(text=h[I])
	for I in K(9):A[I]=F
	E(D,4,6,text=X,bg=W,width=0,height=0);E(C,0,9,state=L,text=X);E(C,12,14,state=S);E(C,10,12,state=L);R.config(text=X);G=H;B=H
def p():
	B='s';C=A[0]==A[1]==A[2]!=F;E=A[3]==A[4]==A[5]!=F;G=A[6]==A[7]==A[8]!=F
	if C:D[4].grid(row=3,sticky=B,columnspan=3,rowspan=2,pady=140);return A[0]
	elif E:D[4].grid(row=3,sticky=B,columnspan=3,rowspan=3,pady=140);return A[3]
	elif G:D[4].grid(row=3,sticky=B,columnspan=3,rowspan=4,pady=140);return A[6]
def q():
	B='e';C=A[0]==A[3]==A[6]!=F;E=A[1]==A[4]==A[7]!=F;G=A[2]==A[5]==A[8]!=F
	if C:D[5].grid(row=4,sticky=B,rowspan=3,padx=170,columnspan=1);return A[0]
	elif E:D[5].grid(row=4,sticky=B,rowspan=3,padx=173,columnspan=2);return A[1]
	elif G:D[5].grid(row=4,sticky=B,rowspan=3,padx=173,columnspan=3);return A[2]
def r():
	B=A[0]==A[4]==A[8]!=F;C=A[2]==A[4]==A[6]!=F
	if B:return A[0]
	elif C:return A[2]
def s():
	global G;A=p();B=q();C=r()
	if A:D[4].config(text='_',width=330,bg=a);G=A
	elif B:D[5].config(text='|',bg=a,width=3,height=116);G=B
	elif C:G=C
def e():pass
def t(Button,Position):
	H=Position;D=Button;global B
	if B==Y:
		if A[H]==F:A[H]=B;D.config(command=e,state=L)
		D.config(text=B,fg='yellow',state=S);B=Z
	elif B==Z:
		if A[H]==F:A[H]=B;D.config(command=e,state=L)
		D.config(text=B,fg='orange',state=S);B=Y
	R.config(text=f"{B}'s Turn")
	if F not in A:R.config(text="It's A Tie");E(C,10,12,state=S)
	s()
	if G==Y or G==Z:R.config(text=f"{G} WON ");E(C,10,12,state=S);E(C,0,9,co=e)
def f(Player):
	global B
	for A in K(9):C[A].config(command=lambda i=A:t(C[i],i))
	E(C,0,9,state=S);E(C,12,14,state=L);B=Player;R.config(text=f"{B}'s Turn")
for J in h:u=d(I,text=J,fg=a,bg=W,font=(b,10,c));D.append(u)
k=[(9,10,11,12,13),(I.destroy,n,o,lambda:f(Q[0]),lambda:f(Q[1]))]
for (v,w,x,y) in V([[X]*9,['EXIT','REMATCH','RESTART',Q[0],Q[1]]],[[2]*9,[0]*5],[[30]*9,[5]*5],[[30]*9,[15]*5]):
	for (z,A0,A1,A2) in V(v,w,x,y):A3=l(I,text=z,bg=W,fg=a,width=A0,font=(b,A1,c),state=L,bd=A2);C.append(A3)
for J in K(5):C[k[0][J]].config(state=S,command=k[1][J])
E(C,10,12,state=L)
E(C,12,14,font=(b,9,c))
for J in K(2):A4=d(I,font=(b,1,c));D.append(A4)
R=d(I,fg=a,bg=W,font=(b,15,c))
for (T,U,g) in V([0,1,3,3],[1,1,0,1],[1,1,2,2]):j+=1;D[j].grid(row=T,column=U,columnspan=g)
R.grid(row=2,column=1,pady=70)
for J in [[4]*3,[5]*3,[6]*3]:
	for (T,U) in V(J,[0,1,2]*3):i+=1;C[i].grid(row=T,column=U)
for (A5,T,U,g,A6) in V([10,11,12,13,9],[8,8,10,10,11],[0,2,0,1,1],[1,1,2,2,1],[45,50,50,50,50]):C[A5].grid(row=T,column=U,columnspan=g,ipadx=A6,pady=50)
I.mainloop()
