
# Criar um vetor vazio para armazenar os valores pares
vetor_par = []

# Criar um vetor vazio para armazenar os valores ímpares
vetor_impar = []

# Loop para ler os valores do vetor
for i in range(10):
    valor = int(input("Digite um valor inteiro: "))
    
    if valor % 2 == 0:
        # Se o valor é par, adiciona ao vetor_par
        vetor_par.append(valor)
    else:
        # Se o valor é ímpar, adiciona ao vetor_impar
        vetor_impar.append(valor)

# Imprimir o vetor par
print("Vetor par:", vetor_par)

# Imprimir o vetor ímpar
print("Vetor ímpar:", vetor_impar)
