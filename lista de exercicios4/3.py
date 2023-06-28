import random

vetor = []
vetor2 = []
vetor3 = []
vetor4 = []
vetor5 = []

for i in range(10):
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    vetor.append(a)
    vetor2.append(b)

for i in range(10):
    c = vetor[i] - vetor2[i]
    vetor3.append(c)

for i in range(10):
    d = vetor[i] + vetor2[i]
    vetor4.append(d)

for i in range(10):
    e = vetor[i] * vetor2[i]
    vetor5.append(e)

print(vetor)
print(vetor2)
print(vetor3)
print(vetor4)
print(vetor5)
