def trocar_elementos(vetor):
    tamanho = len(vetor)
    for i in range(tamanho // 2):
        vetor[i], vetor[tamanho - 1 - i] = vetor[tamanho - 1 - i], vetor[i]

# Leitura do vetor
vetor = []

print("Digite os valores do vetor (20 elementos):")
for i in range(20):
    numero = int(input())
    vetor.append(numero)

# Impressão do vetor original
print("Vetor original:")
print(vetor)

# Troca dos elementos
trocar_elementos(vetor)

# Impressão do vetor após a troca
print("Vetor após a troca:", vetor)