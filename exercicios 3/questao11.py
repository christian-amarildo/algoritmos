# Elabore um algoritmo que leia uma série de 50 notas e calcule quantas estão
# 10% acima da média e quantas estão 10% abaixo da média.
notas = []
soma = 0
# Leitura das 50 notas
for i in range(50):
    nota = int(input("insira a nota "))
    notas.append(nota)
    soma += nota

media = soma / 50

# Contagem das notas acima e abaixo da média
acima_media = 0
abaixo_media = 0
for nota in notas:
    if nota > media:
        acima_media += 1
    else:
        abaixo_media += 1

# Exibição dos resultados
print("Quantidade de notas acima da média: ", acima_media)
print("Quantidade de notas abaixo da média: ", abaixo_media)
