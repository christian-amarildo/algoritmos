from dataclasses import dataclass
@dataclass
class Regtesla:
    id: int
    marca:str
    modelo: str
    preco: int

N=int(input(f"\nQuantos veículos serão registrados?: \n"))
lista=[None]*N
for i in range(N):
    lista[i]=Regtesla(0,'','',0)

print('\nIniciando Registros:\n')

for i in range(N):
    print(f'\n{i+1}° Veículo ')
    lista[i].modelo=input('Modelo: ')
    lista[i].marca=input('Marca: ')
    lista[i].id=int(input('Id: '))
    lista[i].preco=int(input('Preço: R$'))


op=''
while op!="N":
    op=input('''
    Deseja fazer alguma operação?[S/N](Maiusculo): ''')
    if op=='S':
        acao=input('''
        Qual a ação?:
        [A] Buscar por ID
        [B] Atualizar o Preço de um veículo
        [C]Remover veículo da base de dados
        Sua opção?(Digite corretamente): ''')
        if acao=="A":
            ID=int(input("Qual o id do veiculo?: \n"))
            for i in range (N):
                if lista[i].id==ID:
                    print(f'''
                    Modelo: {lista[i].modelo}
                    Marca: {lista[i].marca}
                    ID: {lista[i].id}
                    Preço: {lista[i].preco}
                    ''')
                if lista[i].id==0:
                    print('\nVeículo não está na base de dados\n')
        if acao=="B":
            ID=int(input("Qual o id do veiculo?: \n"))
            for i in range (N):
                if lista[i].id==ID:
                    lista[i].preco=int(input("Digite o novo preço: R$"))
                    print('Preço atualizado')
        
        if acao=="C":
            ID=int(input("Qual o id do veiculo?: \n"))
            for i in range (N):
                if lista[i].id==ID:
                    lista[i]=Regtesla(0,'','',0)
                    print('Informações Excluidas')




