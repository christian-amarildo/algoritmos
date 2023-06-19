count = 0

while True:
    num = int(input("Digite um número positivo (ou um número negativo para parar): "))
    
    if num < 0:
        break
    else:
        count += 1

print("Foram digitados", count, "números.")
