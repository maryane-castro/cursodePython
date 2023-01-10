'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados
de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas;
B) A média de idade do grupo;
C) Uma lista com todas as mulheres;
D) Uma lista com todas as pessoas com idade acima da média.'''
pessoas = []
media = 0
dados = {}
cont = ''
while cont != 'N':
    dados['nome'] = str(input('Nome: ')).title()
    dados['sexo'] = str(input('Sexo[M/F]: ')).upper()
    dados['idade'] = float(input('Idade: '))
    pessoas.append(dados.copy())
    while True:
        cont = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
        if cont not in 'SN':
            print('Erro! Tente novamente.')
        else:
            break
print('-='* 30)
for pessoa in pessoas:
    media += pessoa['idade']
media = media / len(pessoas)
print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'- A média de idade é {media} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'], end=' ')
print()
print(f'- Lista das pessoas com idade assima da media:')
for pessoa in pessoas:
    if pessoa['idade'] > media:
        print(f"Nome: {pessoa['nome']}| Sexo: {pessoa['sexo']}| Idade: {pessoa['idade']}")
print('<<ENCERRADO>>')