from dataclasses import dataclass
@dataclass
class Regpaciente:
    id: int
    nome:str
    doenca: str
    idade: int

N=int(input(f"\nQuantos pacientes serão registrados?: \n"))
lista=[None]*N
for i in range(N):
    lista[i]=Regpaciente(0,'','',-1)

print('\nIniciando Registros:\n')

for i in range(N):
    print(f'\n{i+1}° Paciente ')
    lista[i].nome=input('Nome: ')
    lista[i].doenca=input('Doença: ')
    lista[i].id=int(input('Id: '))
    lista[i].idade=int(input('Idade: '))
soma=0
cont=0

op=''
while op!="N":
    op=input('''
    Deseja fazer alguma operação?[S/N](Maiusculo): ''')
    if op=='S':
        acao=input('''
        Qual a ação?:
        [A] Buscar por ID
        [B] Atualizar doença de paciente
        [C]Remover paciente da base de dados
        [D]Média das idades
        Sua opção?(Digite corretamente): ''')
        if acao=="A":
            ID=int(input("Qual o id do paciente?: \n"))
            for i in range (N):
                if lista[i].id==ID:
                    print(f'''
                    Nome: {lista[i].nome}
                    Doença: {lista[i].doenca}
                    ID: {lista[i].id}
                    Idade: {lista[i].idade}
                    ''')
                if lista[i].id==0:
                    print('\nPaciente não está na base de dados\n')
        if acao=="B":
            ID=int(input("Qual o id do Paciente?: \n"))
            for i in range (N):
                if lista[i].id==ID:
                    lista[i].doenca=input("Digite a nova doença do paciente?: ")
                    print('Doença atualizado')
        
        if acao=="C":
            ID=int(input("Qual o id do paciente?: \n"))
            for i in range (N):
                if lista[i].id==ID:
                    lista[i]=Regpaciente(0,'','',-1)
                    print('Informações Excluidas')
        if acao=="D":
            cont=0
            soma=0
            for i in range (len(lista)):
                if lista[i].idade!=-1:
                    soma+=lista[i].idade
                    cont+=1
            print(f'A média das idades é: {soma/cont}')

print('\nPrograma Encerrado\n')





