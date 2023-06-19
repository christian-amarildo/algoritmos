# Sendo H = 1 + 1/2 + 1/3 + 1/4 +...+ 1/N. Escreva um algoritmo para gerar o
# número H. O número N é fornecido pelo usuário.

# Leitura do valor de N fornecido pelo usuário
N = int(input("Digite o valor de N: "))

# Inicialização da variável H
H = 1

# Loop para calcular o valor de H
for i in range(1, N):
    H += 1 / (1+i)

# Exibição do resultado
print("O valor de H = 1 + 1/2 + 1/3 + 1/4 +...+ 1/N É : ", H)
