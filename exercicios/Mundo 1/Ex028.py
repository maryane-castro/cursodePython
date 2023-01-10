#Escreva um programa que faça o compumputdor pensar em um numero entre 0 e 5 e peça para o usuario tentar adivinhar qual é o numero
#O programa devera escrever na tela se o usuario venceu ou perdeu
from random import randint
from math import floor
comp = floor(randint(0, 5))
resp = int(input('O computador esta pensando um um numero entre 0 e 5, tente adivinhar qual é:  '))
print('PARABENS!!! Voce acertou!' if resp == comp else 'Voce errou! O numero certo era {}.Tente de novo.'.format(comp)) 
