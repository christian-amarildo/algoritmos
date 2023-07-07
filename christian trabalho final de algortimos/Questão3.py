Matriz=[[0,0,0],[0,0,0],[0,0,0]]
Matrizsoma=[[0,0,0],[0,0,0],[0,0,0]]
print('\nPreencha uma matriz 3x3:\n')
for l in range (3):
    for c in range (3):
        Matriz[l][c]=int(input(f"Qual o valor de coordenadas [{l+1},{c+1}]?: "))

print('\nMatriz Formada Original:\n')
for l in range (3):
    for c in range (3):
        print(f'[{Matriz[l][c]:^5}]', end=" ")

    print()

for L in range (3):
    for C in range (3):
        for linha in range (3):
            for coluna in range (3):
                if L<=linha and C<=coluna:
                    Matrizsoma[linha][coluna]+=Matriz[L][C]

print(f'\nA Matriz Soma Cumulativa formada é: \n\n')
for l in range (3):
    for c in range (3):
        print(f'[{Matrizsoma[l][c]:^5}]', end=" ")

    print()
