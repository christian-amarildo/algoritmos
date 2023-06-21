def encontrar_menor_elemento(vetor):
    menor = vetor[0]
    posicao = 0

    for i in range(1, len(vetor)):
        if vetor[i] < menor:
            menor = vetor[i]
            posicao = i

    return menor, posicao


# Leitura do vetor
vetor = []
for i in range(20):
    elemento = int(input("Digite um número: "))
    vetor.append(elemento)

# Encontrar o menor elemento e sua posição
menor_elemento, posicao = encontrar_menor_elemento(vetor)

# Exibir o resultado
print("O menor elemento de N é", menor_elemento, "e sua posição dentro do vetor é:", posicao)
