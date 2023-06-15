valor1 = float(input("digite um numero\n"))
valor2 = float(input("digite um numero\n"))
if valor2 < 0:
    print("operação parou")
    print("quantidade de media=0")
else:
    media = (valor1 + valor2)/2
    quantidade = 1
    print(media)

while valor2 >= 0:
    valor2 = float(input("insira outro valor para ser feito a media\n"))
    if valor2 < 0:
        break
    media = (media + valor2)/2
    quantidade = quantidade + 1
    print(media)
print(f'quantidade de medias feitas {quantidade}')
