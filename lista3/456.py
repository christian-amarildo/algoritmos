#04
tempo =  int(input("Digite o tempo da viagem\n"))
velocidade =  int(input("Digite a velocidade\n"))

distancia = tempo * velocidade
litrosUsados = distancia/12

print(f"o tempo gasto na viagem foi {tempo}, a velocidade média foi {velocidade}, a distância pecorrida foi {distancia}, e a quantidade de litros usados foi {litrosUsados}")

#05
pao = float(input("qual a quantidade de pão vendidos?\n"))
bolo = float(input("qual a quantidade de bolo vendidos?\n"))

pao = pao * 0.12
bolo = bolo * 10.50

arrecadaçao = pao + bolo
poupança = arrecadaçao * 0.1

print(f"A receita da venda de pão e bolo deu {arrecadaçao}, e o dinheiro a ser depositado na poupança é {poupança}")

#06
a = int(input("Digite o valor de a\n"))
b = int(input("Digite o valor de b\n"))

c = a
d = b

print("invertendo")

print(f"o valor de a é {d}, o valor de b é {c}")