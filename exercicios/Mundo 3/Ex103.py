'''Faça um programa que tenha uma função chamada ficha(), que receba dois 
parametros opcionais: o nome de um jogador e quantos gols ele marcou.

O progama deverá ser capaz de mostrar a ficha do jogador, mesmo que 
algum dado não tenha sido informado corretamente.'''

print('\n\n','-'*30)
def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {nome.title()} fez {gols} gol(s) no campeonato.')


ficha(input('Nome do jogador:  '), input('Número de gols:  '))