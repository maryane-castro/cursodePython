#Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador PERDER.
# mostrando o total de vitorias consecutivas que ele conquistou no final do jogo
from random import randint
comp = randint(0,10)
c = 0
enf = '-=' * 20
while True:
    print(enf)
    num = int(input('Digite um numero:  '))
    parin = input('Par ou impar?[P/I]  ').upper()
    print(enf)
    s = comp + num
    if parin != 'P' and parin != 'I':
        print('Erro! Tente novamente.')
        break
    if s % 2 == 0:
        deu = 'DEU PAR'
    else:
        deu = 'DEU IMPAR'
    print(f'Voce jogou {num} e o computador {comp}. Total {s} {deu}.')
    if parin == 'P' and deu == 'DEU PAR' or parin == 'I' and deu == 'DEU IMPAR':
        print('VOCE GANHOU!')
        c += 1
    else:
        print('VOCE PERDEU!')
        break
print(enf)
print(f'Game Over! Voce ganhou {c} vez(es).')
