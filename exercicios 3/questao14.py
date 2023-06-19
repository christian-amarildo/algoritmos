# Escreva um algoritmo que leia o número de linhas (n) que o usuário deseja e
# então exiba o Triângulo de Pascal com n linhas.
# Exemplo para n = 6, temos:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
def calcular_coeficiente(i, j):
    if j == 0 or j == i:
        return 1
    else:
        return calcular_coeficiente(i-1, j-1) + calcular_coeficiente(i-1, j)


def exibir_triangulo_pascal(n):
    for i in range(n):
        for j in range(i + 1):
            coeficiente = calcular_coeficiente(i, j)
            print(coeficiente, end=' ')
        print()

# Leitura do número de linhas


n = int(input("Digite o número de linhas: "))

# Exibição do Triângulo de Pascal
exibir_triangulo_pascal(n)
