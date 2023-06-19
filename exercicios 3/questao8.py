# Função para calcular o MDC (Máximo Divisor Comum)
def calcular_mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Função para calcular o MMC (Mínimo Múltiplo Comum)
def calcular_mmc(a, b):
    return abs(a * b) // calcular_mdc(a, b)

# Leitura dos dois números fornecidos pelo usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Cálculo do MMC
mmc = calcular_mmc(num1, num2)

# Exibição do resultado
print("O Mínimo Múltiplo Comum (MMC) entre", num1, "e", num2, "é:", mmc)