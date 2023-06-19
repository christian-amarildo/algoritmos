
soma = 0
contador = 0

while True:
    numero = float(input("Digite um número positivo (ou um número negativo para encerrar): "))
    
    if numero < 0:
        break
    
    soma += numero
    contador += 1

if contador > 0:
    media = soma / contador
    print("A média dos números digitados é:", media)
else:
    print("Nenhum número válido foi digitado.")
