# Função para calcular o MDC (Máximo Divisor Comum)
def calcular_mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Leitura dos dois números fornecidos pelo usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Cálculo do MDC
mdc = calcular_mdc(num1, num2)

# Exibição do resultado
print("O Máximo Divisor Comum (MDC) entre", num1, "e", num2, "é:", mdc)
