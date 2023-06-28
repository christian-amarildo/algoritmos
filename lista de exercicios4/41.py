matriz = []
matriz2 = []
result = []

# Preenchendo a primeira matriz
for i in range(2):
    linha = []
    for j in range(3):
        a = int(input("Insira o valor da primeira matriz: "))
        linha.append(a)
    matriz.append(linha)

# Preenchendo a segunda matriz
for i in range(2):
    linha = []
    for j in range(3):
        b = int(input("Insira o valor da segunda matriz: "))
        linha.append(b)
    matriz2.append(linha)

# Somando as matrizes
for i in range(2):
    linha_result = []
    for j in range(3):
        c = matriz[i][j] + matriz2[i][j]
        linha_result.append(c)
    result.append(linha_result)

# Imprimindo as matrizes e o resultado
print("Matriz 1:")
for linha in matriz:
    print(linha)

print("Matriz 2:")
for linha in matriz2:
    print(linha)

print("Resultado:")
for linha in result:
    print(linha)
