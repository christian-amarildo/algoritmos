# Escreva um algoritmo que leia um vetor de 12 números inteiros e crie um
# segundo vetor a partir dos elementos armazenados nas posições ímpares do
# primeiro vetor. Mostre em saída padrão os dois vetores.

vetor = []
vetor2 = []
vetor3 = []
for i in range(12):
    vector = int(input("insira os 12 vetores"))
    vetor.append(vector)

for vector in vetor:
    if vector % 2 == 1:
        vetor2.append(vector)
    else:
        vetor3.append(vector)

print("o vetor original é ", vetor)
print("o vetor impar é ", vetor2)
print("o vetor par é ", vetor3)
