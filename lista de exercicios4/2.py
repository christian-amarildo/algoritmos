vetor = []
vetorpar = []
vetorimpar = []

for i in range(20):
    a = int(input("insira um valor inteiro :"))
    vetor.append(a)

for a in vetor:
    if a % 2 == 0:
        vetorpar.append(a)
    elif a % 2 == 1:
        vetorimpar.append(a)

vetorpar = sorted(vetorpar)
vetorimpar = sorted(vetorimpar)

print(vetor)
print(vetorpar)
print(vetorimpar)
