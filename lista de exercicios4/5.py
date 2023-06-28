matriz = []
matriz2 = []
matriz3 = []
for i in range(5):
    for j in range(5):
        a = input("insira o valor")
        matriz.append(a)

for i in range(5):
    linha_result = []
    for j in range(5):
        if i == j:
        c = matriz[i][j] + matriz2[i][j]
        linha_result.append(c)
    result.append(linha_result)

print(matriz)
print(matriz2)
print(matriz3)
