vetor = []
vetor2 = []
vetor3 = []

for i in range(10):
    a = int(input("insira um valor inteiro e positivo :"))
    vetor.append(a)

for a in vetor:
    b = a//2
    vetor2.append(b)
    c = a*3
    vetor3.append(c)

print(vetor)
print(vetor2)
print(vetor3)
