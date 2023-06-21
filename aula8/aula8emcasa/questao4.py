def calcular_media(vetor):
    tamanho = len(vetor)
    soma = sum(vetor)
    media = soma / tamanho
    return media

def calcular_vetor_diferenca(vetor, media):
    vetor_diferenca = []
    for valor in vetor:
        diferenca = valor - media
        vetor_diferenca.append(diferenca)
    return vetor_diferenca

# Leitura do tamanho do vetor
N = int(input("Digite o tamanho do vetor: "))

# Leitura dos valores do vetor
vetor = []
print(f"Digite os {N} valores do vetor:")
for _ in range(N):
    valor = int(input())
    vetor.append(valor)

# Cálculo da média
media = calcular_media(vetor)
print("Média:", media)

# Cálculo do vetor de diferença
vetor_diferenca = calcular_vetor_diferenca(vetor, media)
print("Vetor de diferença:")
print(vetor_diferenca)
