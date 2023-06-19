# Função para calcular o número de grãos recebidos pelo monge
def calcular_graos():
    num_quadros = 64  # Total de quadros no tabuleiro de xadrez
    graos_total = 0

    for quadro in range(num_quadros):
        graos_quadro = 2 ** quadro
        graos_total += graos_quadro

    return graos_total

# Chamada da função e exibição do resultado
total_graos = calcular_graos()
print("O monge espera receber um total de", total_graos, "grãos de trigo.")
