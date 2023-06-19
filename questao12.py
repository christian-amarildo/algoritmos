# Dado um vetor de 50 alturas, faça um algoritmo que permita calcular:
# a. A média das alturas.
# b. O desvio padrão das alturas. Lembrando que desvio padrão é dado por
# √(((∑(Altura - média)
# 2
# )/número de alturas)
# c. A moda das alturas. Lembrando que moda é o valor de maior incidência
# de repetições na amostra.
# d. A mediana das alturas. Lembrando que mediana é o elemento central de
# uma lista ordenada.


altura = []
soma = 0

# Entrada das alturas
for i in range(50):
    h = float(input("Insira a altura: "))
    altura.append(h)
    soma += h

media = soma / 50

# Cálculo do desvio padrão
soma_diferencas_quadrado = 0
for h in altura:
    soma_diferencas_quadrado += (h - media) ** 2

desvio_padrao = (soma_diferencas_quadrado / 50) ** 0.5

# Cálculo da moda
frequencia = {}
for h in altura:
    if h in frequencia:
        frequencia[h] += 1
    else:
        frequencia[h] = 1

moda = max(frequencia, key=frequencia.get)

# Cálculo da mediana
altura_ordenada = sorted(altura)
mediana = altura_ordenada[25]

# Exibição dos resultados
print("Média das alturas:", media)
print("Desvio padrão das alturas:", desvio_padrao)
print("Moda das alturas:", moda)
print("Mediana das alturas:", mediana)
