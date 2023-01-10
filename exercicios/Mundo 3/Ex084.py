#Faça um programa que leia nome e peso de varias pessoas, quardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves. 
pessoas = []
info = []
cont = ''
maior = menor = 0
while cont != 'N':
    nome = str(input('Nome:  ')).title()
    peso = int(input('Peso:  '))
    info.extend([nome, peso])
    pessoas.append(info[:])
    info.clear()
    while True:
        cont = str(input('Quer continuar?  ')).upper().strip()[0]
        if cont not in 'SN':
            print('Erro! Resposta invalida, Tente novamente: ')
        else:
            break
for ind, p in enumerate(pessoas):
    if ind == 0:
        maior = p[1]
        menor = p[1]
    elif maior < p[1]:
        maior = p[1]
    elif menor > p[1]:
        menor = p[1]
print('-='*25)
print(f'{len(pessoas)} pessoas foram cadastradas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end='... ')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(p[0], end='... ')
print()