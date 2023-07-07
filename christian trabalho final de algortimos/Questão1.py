Vet=[]
N=0
while True:
    N=int(input("Digite um número para compor o vetor (digite -99 para sair do loop): "))
    if N!= -99:
        Vet.append(N)
    else:
        break
Num=int(input('\nAgora, qual é seu número Alvo?: '))
print(f'''\nVetor= {Vet}
Número Alvo = {Num}

Pares Formados: ''')
for i in range (len(Vet)):
    for j in range (i, len(Vet),1):
        if Vet[i]+Vet[j]==Num:
            print(f'({Vet[i]}, {Vet[j]}) por que {Vet[i]}+{Vet[j]}={Num}')

