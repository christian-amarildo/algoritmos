# Elabore um algoritmo que calcule N! (fatorial de N), sendo que o valor inteiro
# de N é fornecido pelo usuário. Sabendo que:
# N! = 1 * 2 * 3 *...* (N-1) * N
# 0! = 1, por definição.

# Leitura do valor de N fornecido pelo usuário
N = int(input("Digite o valor de N: "))

# Verificação se o valor de N é válido
if N < 0:
    print("Valor inválido. O fatorial não pode ser calculado para valores negativos.")
elif N == 0:
    fatorial = 1
else:

    fatorial = 1

    # Cálculo do fatorial
    for i in range(1, N+1):
        fatorial = i*fatorial

    # Exibição do resultado
    print("O fatorial de", N, "é:", fatorial)


