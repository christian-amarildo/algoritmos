def somar_vetores(vetor1, vetor2):
    resultado = []
    for i in range(len(vetor1)):
        soma = vetor1[i] + vetor2[i]
        resultado.append(soma)
    return resultado

# Leitura dos vetores
vetor1 = []
vetor2 = []

print("Digite os valores do primeiro vetor:")
for i in range(10):
    numero = float(input())
    vetor1.append(numero)

print("Digite os valores do segundo vetor:")
for i in range(10):
    numero = float(input())
    vetor2.append(numero)

# Soma dos vetores
resultado = somar_vetores(vetor1, vetor2)

# Impressão do resultado
print("Resultado da soma dos vetores:")
print(resultado)
