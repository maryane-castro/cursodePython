#Crie um programa ondde 4 jogadore sjoguem um dado e tenham resultados aleatorios. Guarde esses resulatdos me um dicionario.
# No final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior numero no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
print('Valores sorteados: ')
for jog, num in jogo.items():
    print(f'{jog.title()} tirou {num} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse = True)
for ix, num in enumerate(ranking):
    print(f'{ix+1}° lugar: {num[0]} com {num[1]}')
