populacao_a = 35000000
populacao_b = 48000000
taxa_natalidade_a = 0.03
taxa_natalidade_b = 0.02
anos = 0

while populacao_a <= populacao_b:
    populacao_a += populacao_a * taxa_natalidade_a
    populacao_b += populacao_b * taxa_natalidade_b
    anos += 1

print("A população do país A ultrapassará a população do país B em", anos, "anos.")
