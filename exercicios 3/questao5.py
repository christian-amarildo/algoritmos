n = int(input("Digite o valor de n (maior que 1 e inteiro): "))
b = int(input("Digite o valor de b (maior ou igual a 2 e inteiro): "))

if n <= 1 or b < 2:
    print("Valores inválidos!")
else:
    resultado = b ** n
    print("O valor de b^n é:", resultado)
