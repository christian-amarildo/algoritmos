matriz = []
matriz2 = []
# result = []
c = []
for i in range(2):
    for j in range(3):
        a = input("insira o valor das matrizes")
        matriz.append(a)

for i in range(2):
    for j in range(3):
        b = input("insira o valor das matrizes")
        matriz2.append(b)

for i in range(2):
    for j in range(3):
        c[i][j] = matriz[i][j] + matriz2[i][j]
#  result.append(c)

print(matriz)
print(matriz2)
print(c)
