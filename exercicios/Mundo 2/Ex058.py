#Melhore o jogo do desafio 028 onde o computador vai pensar em um numero entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer. 
from random import randint
comp = randint(0, 10)
palp = 0
player = ''
while player != comp:
    player = int(input('Digite um numero entre 0 a 10:  '))
    if player > 10 or player < 0:
        print('Erro! Digite um numero de 0 a 10.')
    else: 
        palp += 1
        if player == comp:
            print('\033[1;32mParabens! voce acertou! O numero que eu pensei foi {}!\033[m'.format(comp))
        else:
            print('\033[31mErrou! Tente novamente.\033[m')
print('Voce acertou depois de {} palpites!'.format(palp))