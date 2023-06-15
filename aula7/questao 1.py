numeros = []
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

print("Números em ordem decrescente:")
for i in range(9, -1, -1):
    print(numeros[i])
