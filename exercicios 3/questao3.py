count_menores = 0
count_maiores = 0

while True:
    idade = int(input("Digite a idade (ou um número negativo para parar): "))
    
    if idade < 0:
        break
    
    if idade < 18:
        count_menores += 1
    elif idade > 60:
        count_maiores += 1

print("Total de pessoas menores de 18 anos:", count_menores)
print("Total de pessoas maiores de 60 anos:", count_maiores)
