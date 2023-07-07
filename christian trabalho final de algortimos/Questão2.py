N=int(input("Qual é o tamanho de sua Matriz NxN ?: "))
Matriz=[]
for i in range (N):
    Matriz.append([0]*N)

IniL, FimL=0, N-1
IniC, FimC=0, N-1
Cont=1
J=0

while Cont<=N**2 :
    if Cont>N**2:
        break
    for i in range (IniC,FimC+1):
        Matriz[IniL][i]=Cont
        Cont+=1
    if Cont>N**2:
        break

    for i in range (IniL+1,FimL+1):
        Matriz[i][FimL]=Cont
        Cont+=1
    if Cont>N**2:
        break

    for i in range (FimC-1,IniC-1,-1):
        Matriz[FimL][i]=Cont
        Cont+=1
    if Cont>N**2:
        break

    for i in range (FimL-1,IniL,-1):
        Matriz[i][IniC]=Cont
        Cont+=1
    if Cont>N**2:
        break
    
    IniL+=1
    IniC+=1
    FimL-=1
    FimC-=1



print(Cont)

for i in range (N):
    print(Matriz[i])
